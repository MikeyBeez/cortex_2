# Core API

The main API for interacting with Cortex_2.

## Initialization

```python
from cortex import Cortex

# Basic initialization
cortex = Cortex()

# With configuration
cortex = Cortex(
    config_file="config/cortex.yaml",
    memory_limit=100000,  # tokens
    auto_load=True
)
```

## Basic Operations

### Process Input
```python
# Simple processing
response = cortex.process("Help me write a Python function")

# With context hints
response = cortex.process(
    input_text="Debug this code",
    context_hints={"domain": "programming", "language": "python"}
)

# Streaming response
for chunk in cortex.process_stream("Explain quantum computing"):
    print(chunk, end="")
```

### Module Management
```python
# Manual module loading
cortex.load_module("python_expertise")
cortex.unload_module("creative_writing")

# List loaded modules
modules = cortex.list_loaded_modules()

# Check if module is loaded
if cortex.is_module_loaded("python_expertise"):
    print("Python module active")
```

### Resource Management
```python
# Get current usage
usage = cortex.get_memory_usage()
print(f"Using {usage.tokens} of {usage.limit} tokens")

# Set memory limit
cortex.set_memory_limit(150000)

# Force cleanup
cortex.cleanup_memory(target_free=20000)
```

## Configuration

### Runtime Configuration
```python
# Enable/disable features
cortex.enable_auto_loading()
cortex.disable_learning()

# Set behavior
cortex.set_optimization_mode("memory")  # or "speed", "balanced"
cortex.set_eviction_strategy("lru")     # or "lfu", "adaptive"
```

### Persistence
```python
# Save state
cortex.save_state("checkpoint.cortex")

# Load state
cortex.load_state("checkpoint.cortex")

# Export configuration
config = cortex.export_config()
cortex.import_config(config)
```

## Advanced Features

### Context Management
```python
# Push context
with cortex.context(domain="web_development"):
    response = cortex.process("How do I set up Django?")

# Context stack
cortex.push_context({"project": "my_app"})
response = cortex.process("What's next?")
cortex.pop_context()
```

### Batch Processing
```python
# Process multiple inputs
inputs = ["Question 1", "Question 2", "Question 3"]
responses = cortex.batch_process(inputs)

# With different contexts
batch = [
    {"input": "Python question", "context": {"domain": "programming"}},
    {"input": "Writing help", "context": {"domain": "creative"}}
]
responses = cortex.batch_process_with_context(batch)
```

## Error Handling

```python
from cortex.exceptions import (
    ModuleNotFoundError,
    InsufficientMemoryError,
    ContextError
)

try:
    cortex.load_module("unknown_module")
except ModuleNotFoundError as e:
    print(f"Module not found: {e}")

try:
    cortex.process("Complex request")
except InsufficientMemoryError as e:
    print(f"Not enough memory: {e}")
    cortex.cleanup_memory()
```

## Callbacks and Hooks

```python
# Module load/unload callbacks
def on_module_loaded(module_id):
    print(f"Loaded: {module_id}")

cortex.on_module_loaded(on_module_loaded)

# Processing hooks
def pre_process(input_text):
    print(f"Processing: {input_text}")
    return input_text  # Can modify

cortex.add_pre_process_hook(pre_process)
```

## System Information

```python
# Get system info
info = cortex.get_system_info()
print(f"Version: {info.version}")
print(f"Modules available: {info.module_count}")
print(f"Memory used: {info.memory_usage}")

# Get statistics
stats = cortex.get_statistics()
print(f"Total processes: {stats.total_processes}")
print(f"Average response time: {stats.avg_response_time}")
```

## Shutdown

```python
# Graceful shutdown
cortex.shutdown()

# With cleanup
cortex.shutdown(save_state=True, cleanup=True)
```

## Response Object

```python
# Response structure
response = cortex.process("Hello")

print(response.text)           # The actual response
print(response.modules_used)   # Which modules were used
print(response.context)        # Detected context
print(response.confidence)     # Confidence score
print(response.metadata)       # Additional info
```

## Next Steps

- See [Module API](module_api.md) for module operations
- See [Identity API](identity_api.md) for identity management
- See [Events API](events_api.md) for event handling
- See [Query API](query_api.md) for searching
