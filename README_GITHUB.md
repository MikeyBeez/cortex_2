# Cortex_2: Cognitive Operating System

A revolutionary cognitive operating system that enables dynamic module loading, identity management, and self-optimizing memory systems for AI applications.

## 🧠 Overview

Cortex_2 reimagines AI memory systems with:
- **Dynamic Module Loading**: Hot-swap cognitive capabilities based on context
- **Identity Management**: Load/unload different identities and personalities  
- **Self-Loading Intelligence**: Automatically loads needed modules based on context
- **Resource Optimization**: Manages memory constraints intelligently
- **Tiered Storage**: Active, warm, and cold storage for efficient access

## 🚀 Quick Start

```bash
# Clone the repository
git clone git@github.com:MikeyBeez/cortex_2.git
cd cortex_2

# Set up environment
./setup.sh

# Start the API server
make dev

# Or run as a service
make service-install
make service-start
```

## 📡 API Access

- **Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│        Cognitive Controller             │
│  (Self-loading intelligence layer)      │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┬─────────┬─────────┐
    ▼                 ▼         ▼         ▼
┌────────┐      ┌─────────┐ ┌───────┐ ┌────────┐
│Identity│      │Module   │ │Memory │ │Resource│
│Manager │      │Registry │ │Layers │ │Monitor │
└────────┘      └─────────┘ └───────┘ └────────┘
```

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Guide](docs/api_guide.md)
- [Module Development](docs/modules.md)
- [Development Guidelines](DEVELOPMENT_GUIDELINES.md)

## 🛠️ Development

```bash
# Run tests
make test

# Format code
make format

# Check service logs
make service-logs
```

## 📦 Key Features

### Module System
- Load specialized expertise on demand
- Automatic dependency resolution
- Version management
- Hot-swapping without restarts

### Knowledge Graph
- Query nodes and edges
- Find paths between concepts
- Extract subgraphs
- Real-time updates

### Identity Management  
- Define core identity components
- Switch between personas
- Preserve identity across sessions
- Composite identities from modules

## 🤝 Integration

- **MCP Server**: Model Context Protocol for Claude integration
- **REST API**: Full OpenAPI 3.0 specification
- **Service**: macOS launchctl integration

## 📄 License

[License information]

## 👤 Author

MikeyBee

---

*Cortex_2: Because intelligence should be dynamic, not static.*
