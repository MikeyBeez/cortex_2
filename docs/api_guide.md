# Cortex_2 API

The Cortex_2 API provides HTTP endpoints for interacting with the cognitive operating system.

## Starting the API Server

```bash
# From the cortex_2 directory
uv run python -m cortex

# Or using uvicorn directly
uv run uvicorn cortex.app:app --reload

# Or using the Makefile
make dev
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## Key Endpoints

### Health Check
- `GET /health` - System health status
- `GET /health/ready` - Readiness check
- `GET /health/live` - Liveness check

### Knowledge Graph
- `GET /knowledge-graph/stats` - Get KG statistics
- `POST /knowledge-graph/query` - Query the knowledge graph
- `POST /knowledge-graph/nodes` - Add a node
- `POST /knowledge-graph/edges` - Add an edge

### Module Management
- `GET /modules` - List all modules
- `POST /modules/load` - Load a module
- `DELETE /modules/{module_id}` - Unload a module

### Context Management
- `POST /context/push` - Push context information
- `POST /context/analyze` - Analyze text for context

### Identity Management
- `GET /identity/current` - Get current identity
- `POST /identity/load/{identity_id}` - Load an identity

### Resource Management
- `GET /resources/memory` - Get memory usage
- `POST /resources/optimize` - Optimize memory

## Testing the API

Run the test script:
```bash
python /Users/bard/Code/cortex_2/tmp/test_api.py
```

Or use curl:
```bash
# Health check
curl http://localhost:8000/health

# Knowledge graph stats
curl http://localhost:8000/knowledge-graph/stats

# Query nodes
curl -X POST http://localhost:8000/knowledge-graph/query \
  -H "Content-Type: application/json" \
  -d '{"query_type": "nodes", "parameters": {}}'
```

## Development

The API is built with FastAPI and uses:
- Pydantic for request/response validation
- Async/await for performance
- Auto-generated OpenAPI documentation

Currently, most endpoints return mock data. As the Cortex_2 implementation progresses, these will be connected to the actual cognitive systems.
