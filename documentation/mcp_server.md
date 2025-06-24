# Cortex_2 MCP Server

Transform Cortex_2 into a Model Context Protocol (MCP) server, enabling Claude and other AI systems to dynamically load cognitive modules based on context.

## Overview

The Cortex_2 MCP server provides:
- Dynamic module loading/unloading
- Context-aware intelligence
- Identity management
- Resource optimization
- Learning from interactions

## Installation

```bash
# Install globally
npm install -g @cortex/mcp-server

# Or use with npx
npx @cortex/mcp-server

# Add to Claude Code
claude mcp add cortex -s user -- npx -y @cortex/mcp-server
```

With custom configuration:
```bash
claude mcp add cortex -s user -- npx -y @cortex/mcp-server \
  --memory-limit 100000 \
  --storage-dir ~/.cortex/storage \
  --auto-load true
```

## MCP Tools Provided

### 1. Module Management

#### load_module
Load a specific module into active memory.
```typescript
{
  name: "load_module",
  description: "Load a cognitive module",
  inputSchema: {
    type: "object",
    properties: {
      module_id: { type: "string" },
      priority: { type: "string", enum: ["low", "normal", "high"] }
    },
    required: ["module_id"]
  }
}
```

#### unload_module
Unload a module from active memory.
```typescript
{
  name: "unload_module",
  description: "Unload a cognitive module",
  inputSchema: {
    type: "object",
    properties: {
      module_id: { type: "string" },
      force: { type: "boolean" }
    },
    required: ["module_id"]
  }
}
```

#### list_modules
List available or loaded modules.
```typescript
{
  name: "list_modules",
  description: "List cognitive modules",
  inputSchema: {
    type: "object",
    properties: {
      filter: { type: "string", enum: ["all", "loaded", "available"] },
      type: { type: "string", enum: ["knowledge", "capability", "identity", "memory"] }
    }
  }
}
```

### 2. Context Management

#### push_context
Push context information to influence module loading.
```typescript
{
  name: "push_context",
  description: "Push context for module selection",
  inputSchema: {
    type: "object",
    properties: {
      domain: { type: "string" },
      keywords: { type: "array", items: { type: "string" } },
      intent: { type: "string" }
    }
  }
}
```

#### analyze_context
Analyze text to determine context and suggest modules.
```typescript
{
  name: "analyze_context",
  description: "Analyze input context",
  inputSchema: {
    type: "object",
    properties: {
      input: { type: "string" }
    },
    required: ["input"]
  }
}
```

### 3. Identity Management

#### load_identity
Load a specific identity configuration.
```typescript
{
  name: "load_identity",
  description: "Load an identity configuration",
  inputSchema: {
    type: "object",
    properties: {
      identity_id: { type: "string" }
    },
    required: ["identity_id"]
  }
}
```

#### apply_persona
Apply a persona overlay to current identity.
```typescript
{
  name: "apply_persona",
  description: "Apply a persona overlay",
  inputSchema: {
    type: "object",
    properties: {
      persona_id: { type: "string" }
    },
    required: ["persona_id"]
  }
}
```

### 4. Resource Monitoring

#### get_memory_usage
Get current memory usage statistics.
```typescript
{
  name: "get_memory_usage",
  description: "Get memory usage statistics",
  inputSchema: {
    type: "object",
    properties: {}
  }
}
```

#### optimize_memory
Trigger memory optimization.
```typescript
{
  name: "optimize_memory",
  description: "Optimize memory usage",
  inputSchema: {
    type: "object",
    properties: {
      target_free: { type: "number" }
    }
  }
}
```

### 5. Learning System

#### provide_feedback
Provide feedback on module effectiveness.
```typescript
{
  name: "provide_feedback",
  description: "Provide feedback on interaction",
  inputSchema: {
    type: "object",
    properties: {
      interaction_id: { type: "string" },
      success: { type: "boolean" },
      modules_helpful: { type: "array", items: { type: "string" } }
    }
  }
}
```

## Resources Provided

The MCP server also provides read-only resources:

### Module Catalog
```typescript
{
  uri: "cortex://modules/catalog",
  name: "Module Catalog",
  description: "Browse all available modules",
  mimeType: "application/json"
}
```

### Current State
```typescript
{
  uri: "cortex://state/current",
  name: "Current State",
  description: "Current system state including loaded modules",
  mimeType: "application/json"
}
```

### Learning Metrics
```typescript
{
  uri: "cortex://metrics/learning",
  name: "Learning Metrics",
  description: "Learning system performance metrics",
  mimeType: "application/json"
}
```

## Usage Examples

### Basic Module Loading
```
Claude: "I need to help with Python code"
MCP: analyze_context("I need to help with Python code")
> Suggests: python_expertise, debugging_tools
MCP: load_module("python_expertise")
> Module loaded successfully
```

### Context-Aware Loading
```
Claude: "Let me analyze this Django project"
MCP: push_context({
  domain: "web_development",
  keywords: ["django", "python", "web"],
  intent: "analysis"
})
MCP: load_module("django_framework")
MCP: load_module("web_security")
```

### Identity Switching
```
Claude: "Switching to creative writing mode"
MCP: apply_persona("creative_writer")
MCP: unload_module("technical_documentation")
MCP: load_module("creative_writing")
MCP: load_module("storytelling")
```

### Resource Management
```
MCP: get_memory_usage()
> { used: 85000, limit: 100000, modules: [...] }
MCP: optimize_memory({ target_free: 30000 })
> Freed 35000 tokens by moving 3 modules to warm storage
```

## Configuration

### Environment Variables
```bash
CORTEX_MEMORY_LIMIT=100000        # Max tokens in memory
CORTEX_STORAGE_DIR=~/.cortex      # Storage directory
CORTEX_AUTO_LOAD=true             # Enable auto-loading
CORTEX_LEARNING_ENABLED=true      # Enable learning
CORTEX_LOG_LEVEL=info             # Logging level
```

### Configuration File
```yaml
# ~/.cortex/config.yaml
memory:
  limit: 100000
  buffer: 5000
  
storage:
  hot_size: 50000
  warm_directory: ~/.cortex/warm
  cold_directory: ~/.cortex/cold
  
learning:
  enabled: true
  exploration_rate: 0.1
  
identity:
  default: "assistant"
  auto_adapt: true
```

## Development

### Running Locally
```bash
# Clone repository
git clone https://github.com/mikeybee/cortex_2
cd cortex_2/mcp_server

# Install dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build
```

### Testing with Claude
```bash
# Start the server
npm start

# In another terminal, add to Claude
claude mcp add cortex-dev -s user -- node ./dist/index.js
```

## Architecture

The MCP server wraps the Cortex_2 Python core:

```
┌─────────────────┐
│   Claude Code   │
├─────────────────┤
│   MCP Protocol  │
├─────────────────┤
│ TypeScript Layer│ ← Handles MCP protocol
├─────────────────┤
│  Python Bridge  │ ← Communicates with core
├─────────────────┤
│  Cortex_2 Core  │ ← Full Python implementation
└─────────────────┘
```

## Advanced Features

### Module Packages
Create and share module packages:
```bash
cortex package create my-modules
cortex package add python_expertise django_framework
cortex package publish my-modules
```

### Custom Modules
Add your own modules:
```bash
cortex module create my_custom_knowledge
cortex module add-knowledge ./data.json
cortex module add-triggers python custom
cortex module register
```

### Learning Export
Export learned patterns:
```bash
cortex learning export patterns.json
cortex learning import colleague_patterns.json
```

## Troubleshooting

### Module Not Loading
```bash
# Check available modules
cortex module list

# Verify module health
cortex module verify python_expertise

# Force reload
cortex module reload python_expertise
```

### Memory Issues
```bash
# Check memory usage
cortex memory status

# Clear cache
cortex memory clear-cache

# Reset to defaults
cortex memory reset
```

## Security

- Modules are sandboxed
- File access requires explicit paths
- Network access is disabled by default
- All modules are signed and verified

## Future Enhancements

1. **Distributed Modules**: Load modules from network
2. **Module Marketplace**: Share community modules  
3. **Team Sync**: Share learning across team
4. **Cloud Backup**: Automatic state backup
5. **Multi-Model Support**: Work with GPT, Gemini, etc.

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](../LICENSE)
