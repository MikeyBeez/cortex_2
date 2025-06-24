"""Knowledge Graph API endpoints"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional, Union
import json
from pathlib import Path

from .models import (
    KnowledgeGraphStats, 
    KnowledgeGraphNode, 
    KnowledgeGraphEdge,
    NodeQueryResponse,
    EdgeQueryResponse,
    SubgraphQueryResponse,
    PathQueryResponse,
    AddNodeResponse,
    AddEdgeResponse
)

router = APIRouter()

class KnowledgeGraphQuery(BaseModel):
    query_type: str = Field(..., description="Type of query: nodes, edges, path, subgraph")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Query parameters")

# Temporary: Load KG from file
def load_knowledge_graph():
    """Load the knowledge graph from storage"""
    kg_path = Path("/Users/bard/mcp/memory_files/graph.json")
    if kg_path.exists():
        with open(kg_path, 'r') as f:
            return json.load(f)
    return {"nodes": [], "edges": [], "metadata": {}}

@router.post("/query", response_model=Union[NodeQueryResponse, EdgeQueryResponse, SubgraphQueryResponse, PathQueryResponse])
async def query_knowledge_graph(query: KnowledgeGraphQuery) -> Union[NodeQueryResponse, EdgeQueryResponse, SubgraphQueryResponse, PathQueryResponse]:
    """Query the knowledge graph"""
    kg = load_knowledge_graph()
    query_type = query.query_type
    params = query.parameters
    
    if query_type == "nodes":
        nodes = kg.get("nodes", [])
        if "type" in params:
            nodes = [n for n in nodes if n.get("type") == params["type"]]
        return NodeQueryResponse(nodes=nodes, count=len(nodes))
    
    elif query_type == "edges":
        edges = kg.get("edges", [])
        if "type" in params:
            edges = [e for e in edges if e.get("type") == params["type"]]
        return EdgeQueryResponse(edges=edges, count=len(edges))
    
    elif query_type == "path":
        source = params.get("source")
        target = params.get("target")
        if not source or not target:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Source and target required for path query"
            )
        return PathQueryResponse(
            path_exists=False,
            path=[],
            message="Path finding not yet implemented"
        )
    
    elif query_type == "subgraph":
        node_id = params.get("node_id")
        depth = params.get("depth", 1)
        if not node_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="node_id required for subgraph query"
            )
        
        nodes = kg.get("nodes", [])
        center_node = next((n for n in nodes if n.get("id") == node_id), None)
        
        if not center_node:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Node {node_id} not found"
            )
        
        edges = kg.get("edges", [])
        connected_edges = [
            e for e in edges 
            if e.get("source") == node_id or e.get("target") == node_id
        ]
        
        return SubgraphQueryResponse(
            center_node=center_node,
            edges=connected_edges,
            depth=depth
        )
    
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown query type: {query_type}"
        )

@router.get("/stats", response_model=KnowledgeGraphStats)
async def knowledge_graph_stats() -> KnowledgeGraphStats:
    """Get knowledge graph statistics"""
    kg = load_knowledge_graph()
    nodes = kg.get("nodes", [])
    edges = kg.get("edges", [])
    
    node_types = {}
    for node in nodes:
        node_type = node.get("type", "unknown")
        node_types[node_type] = node_types.get(node_type, 0) + 1
    
    edge_types = {}
    for edge in edges:
        edge_type = edge.get("type", "unknown")
        edge_types[edge_type] = edge_types.get(edge_type, 0) + 1
    
    return KnowledgeGraphStats(
        total_nodes=len(nodes),
        total_edges=len(edges),
        node_types=node_types,
        edge_types=edge_types,
        metadata=kg.get("metadata", {}),
        last_updated=kg.get("metadata", {}).get("last_updated", "unknown")
    )

@router.post("/nodes", response_model=AddNodeResponse)
async def add_knowledge_node(node: KnowledgeGraphNode) -> AddNodeResponse:
    """Add a node to the knowledge graph"""
    kg = load_knowledge_graph()
    nodes = kg.get("nodes", [])
    
    if any(n.get("id") == node.id for n in nodes):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Node {node.id} already exists"
        )
    
    nodes.append(node.dict())
    # TODO: Save back to storage
    
    return AddNodeResponse(status="added", node_id=node.id)

@router.post("/edges", response_model=AddEdgeResponse)
async def add_knowledge_edge(edge: KnowledgeGraphEdge) -> AddEdgeResponse:
    """Add an edge to the knowledge graph"""
    kg = load_knowledge_graph()
    edges = kg.get("edges", [])
    edges.append(edge.dict())
    # TODO: Save back to storage
    
    return AddEdgeResponse(status="added", edge=f"{edge.source} -> {edge.target}")
