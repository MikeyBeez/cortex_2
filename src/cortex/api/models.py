"""API Response Models"""
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime

# Health models
class ComponentStatus(BaseModel):
    status: str

class HealthStatus(BaseModel):
    status: str
    timestamp: str
    version: str
    components: Dict[str, Dict[str, str]]  # Changed to explicit dict structure

class ReadinessStatus(BaseModel):
    status: str

class LivenessStatus(BaseModel):
    status: str

# Module models
class ModuleInfo(BaseModel):
    id: str
    type: str
    name: str
    description: str
    size_tokens: int
    status: str
    version: Optional[str] = None
    dependencies: List[str] = []

class ModuleLoadResponse(BaseModel):
    status: str
    module_id: str
    message: Optional[str] = None

class ModuleUnloadResponse(BaseModel):
    status: str
    module_id: str

# Knowledge Graph models
class KnowledgeGraphNode(BaseModel):
    id: str
    type: str
    properties: Dict[str, Any]

class KnowledgeGraphEdge(BaseModel):
    source: str
    target: str
    type: str
    properties: Dict[str, Any]

class KnowledgeGraphStats(BaseModel):
    total_nodes: int
    total_edges: int
    node_types: Dict[str, int]
    edge_types: Dict[str, int]
    metadata: Dict[str, Any]
    last_updated: str

class NodeQueryResponse(BaseModel):
    nodes: List[KnowledgeGraphNode]
    count: int

class EdgeQueryResponse(BaseModel):
    edges: List[KnowledgeGraphEdge]
    count: int

class SubgraphQueryResponse(BaseModel):
    center_node: KnowledgeGraphNode
    edges: List[KnowledgeGraphEdge]
    depth: int

class PathQueryResponse(BaseModel):
    path_exists: bool
    path: List[str]
    message: Optional[str] = None

class AddNodeResponse(BaseModel):
    status: str
    node_id: str

class AddEdgeResponse(BaseModel):
    status: str
    edge: str

# Context models
class ContextPushResponse(BaseModel):
    status: str
    domain: str
    intent: str
    keywords: List[str]
    suggested_modules: List[str] = []

class ContextAnalysisResponse(BaseModel):
    keywords: List[str]
    domain: str
    intent: str
    confidence: float
    suggested_modules: List[str] = []

# Identity models
class IdentityInfo(BaseModel):
    identity_id: str
    traits: List[str]
    communication_style: Optional[Dict[str, str]] = None
    active_personas: List[str] = []

class IdentityLoadResponse(BaseModel):
    status: str
    identity_id: str
    message: str

# Resource models
class ModuleMemoryInfo(BaseModel):
    id: str
    size_tokens: int
    loaded_at: Optional[str] = None

class MemoryUsageResponse(BaseModel):
    used_tokens: int
    limit_tokens: int
    free_tokens: int
    usage_percentage: float
    loaded_modules: List[ModuleMemoryInfo] = []

class MemoryOptimizeResponse(BaseModel):
    status: str
    freed_tokens: int
    modules_unloaded: int

# Root response
class RootResponse(BaseModel):
    name: str
    version: str
    description: str
    docs_url: str
    health_url: str
    modules_url: str
    knowledge_graph_url: str
