# Module API

API for managing and interacting with modules.

## Module Discovery

### Search for Modules
```python
# Search by keyword
modules = cortex.modules.search("python")

# Advanced search
results = cortex.modules.search(
    keywords=["web", "framework"],
    type=ModuleType.KNOWLEDGE,
    min_rating=4.0,
    max_size=50000  # tokens
)

# Search with filters
results = cortex.modules.search_advanced({
    "domain": "programming",
    "tags": ["python", "web"],
    "author": "community",
    "sort": "popularity"
})
```

### Get Module Information
```python
# Get module details
info = cortex.modules.get_info("python_expertise")
print(f"Size: {info.size_tokens} tokens")
print(f"Version: {info.version}")
print(f"Dependencies: {info.dependencies}")

# Get module stats
stats = cortex.modules.get_stats("python_expertise")
print(f"Used {stats.usage_count} times")
print(f"Average load time: {stats.avg_load_time}ms")
```

## Module Loading

### Load Modules
```python
# Simple load
cortex.modules.load("python_expertise")

# Load with options
cortex.modules.load(
    module_id="python_expertise",
    priority="high",
    timeout=5000,  # ms
    fallback="python_basic"
)

# Load multiple
cortex.modules.load_many([
    "python_expertise",
    "debugging_tools",
    "testing_frameworks"
])
```

### Unload Modules
```python
# Simple unload
cortex.modules.unload("creative_writing")

# Force unload (even with dependencies)
cortex.modules.unload("python_expertise", force=True)

# Unload by criteria
cortex.modules.unload_where(
    lambda m: m.last_used < datetime.now() - timedelta(hours=1)
)
```

## Module Dependencies

```python
# Get dependencies
deps = cortex.modules.get_dependencies("django_framework")

# Get full dependency tree
tree = cortex.modules.get_dependency_tree("django_framework")

# Check compatibility
compatible = cortex.modules.check_compatibility(
    "django_framework",
    with_modules=["python_expertise", "web_development"]
)

# Resolve conflicts
conflicts = cortex.modules.find_conflicts()
for conflict in conflicts:
    print(f"{conflict.module1} conflicts with {conflict.module2}")
```

## Module Creation

### Create New Module
```python
# Module builder
builder = cortex.modules.create_builder(
    id="my_custom_module",
    type=ModuleType.KNOWLEDGE
)

# Add content
builder.add_knowledge_file("data/concepts.json")
builder.add_pattern_file("data/patterns.yaml")
builder.add_examples("examples/")

# Set metadata
builder.set_metadata(
    name="My Custom Module",
    description="Domain-specific knowledge",
    author="user@example.com",
    tags=["custom", "domain"]
)

# Add triggers
builder.add_keyword_triggers(["custom", "specific"])
builder.add_pattern_trigger(r"my_pattern.*")

# Build and register
module = builder.build()
cortex.modules.register(module)
```

### Module Validation
```python
# Validate before registration
validation = cortex.modules.validate("path/to/module")
if validation.is_valid:
    cortex.modules.register_from_path("path/to/module")
else:
    for error in validation.errors:
        print(f"Error: {error}")

# Validate loaded module
is_valid = cortex.modules.validate_loaded("my_module")
```

## Module Storage

### Storage Management
```python
# Get storage info
storage = cortex.modules.get_storage_info()
print(f"Hot storage: {storage.hot_modules} modules")
print(f"Warm storage: {storage.warm_modules} modules")
print(f"Cold storage: {storage.cold_modules} modules")

# Move between tiers
cortex.modules.move_to_warm("rarely_used_module")
cortex.modules.move_to_cold(["old_module1", "old_module2"])

# Optimize storage
cortex.modules.optimize_storage()
```

### Import/Export
```python
# Export module
cortex.modules.export(
    module_id="my_module",
    output_path="exports/my_module.cmx"
)

# Import module
cortex.modules.import_module("imports/shared_module.cmx")

# Bulk export
cortex.modules.export_many(
    module_ids=["module1", "module2"],
    output_dir="exports/"
)
```

## Module Lifecycle

### Lifecycle Hooks
```python
# Add lifecycle callbacks
def on_before_load(module_id):
    print(f"Loading {module_id}")

def on_after_load(module_id, load_time):
    print(f"Loaded {module_id} in {load_time}ms")

cortex.modules.add_before_load_hook(on_before_load)
cortex.modules.add_after_load_hook(on_after_load)
```

### Module Events
```python
# Subscribe to module events
cortex.modules.on("module_loaded", handle_load)
cortex.modules.on("module_unloaded", handle_unload)
cortex.modules.on("module_error", handle_error)

# Event data
def handle_load(event):
    print(f"Module: {event.module_id}")
    print(f"Load time: {event.load_time}ms")
    print(f"From tier: {event.storage_tier}")
```

## Module Performance

```python
# Get performance metrics
perf = cortex.modules.get_performance("python_expertise")
print(f"Average load time: {perf.avg_load_time}ms")
print(f"Memory usage: {perf.memory_usage} tokens")
print(f"Cache hit rate: {perf.cache_hit_rate}%")

# Benchmark module
results = cortex.modules.benchmark("python_expertise", iterations=10)
print(f"Load time: {results.load_time_avg}ms ± {results.load_time_std}")
```

## Module Configuration

```python
# Get module config
config = cortex.modules.get_config("python_expertise")

# Update module config
cortex.modules.update_config("python_expertise", {
    "cache_ttl": 3600,
    "preload_on_startup": True,
    "compression": "aggressive"
})

# Reset to defaults
cortex.modules.reset_config("python_expertise")
```

## Error Handling

```python
from cortex.modules.exceptions import (
    ModuleLoadError,
    DependencyError,
    ValidationError
)

try:
    cortex.modules.load("my_module")
except ModuleLoadError as e:
    print(f"Failed to load: {e.reason}")
except DependencyError as e:
    print(f"Missing dependencies: {e.missing}")
```

## Next Steps

- See [Module Creation Guide](../development/module_creation.md)
- See [Module Types](../modules/README.md)
- See [Storage Tiers](../architecture/storage_tiers.md)
