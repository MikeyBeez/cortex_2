# Module Registry

The Module Registry is the central catalog of all available modules in Cortex_2. It tracks metadata, dependencies, and relationships between modules.

## Purpose

- Track all registered modules
- Store module metadata
- Manage dependencies
- Enable module discovery
- Maintain version compatibility

## Core Structure

```python
class ModuleRegistry:
    """Central registry of all modules"""
    
    def __init__(self):
        self.modules = {}  # module_id -> ModuleRecord
        self.index = ModuleIndex()  # For fast searching
        self.dependency_graph = DependencyGraph()
```

## Module Record

Each module is stored with comprehensive metadata:

```python
@dataclass
class ModuleRecord:
    id: str
    version: str
    type: ModuleType
    manifest: ModuleManifest
    location: StorageLocation
    status: ModuleStatus
    stats: ModuleStats
    
@dataclass
class ModuleStats:
    usage_count: int
    last_used: datetime
    avg_load_time: float
    success_rate: float
    size_bytes: int
    compressed_size: int
```

## Key Operations

### Register Module
```python
def register_module(self, module_path: Path) -> ModuleId:
    """Register a new module"""
    # Parse manifest
    manifest = self.parse_manifest(module_path)
    
    # Validate structure
    self.validator.validate(module_path, manifest)
    
    # Check dependencies
    self.verify_dependencies(manifest.dependencies)
    
    # Create record
    record = ModuleRecord(
        id=manifest.id,
        version=manifest.version,
        type=manifest.type,
        manifest=manifest,
        location=self.storage.store(module_path),
        status=ModuleStatus.AVAILABLE,
        stats=ModuleStats()
    )
    
    # Store in registry
    self.modules[record.id] = record
    
    # Update indices
    self.index.add(record)
    self.dependency_graph.add(record)
    
    return record.id
```

### Find Modules
```python
def find_modules(self, criteria: SearchCriteria) -> List[ModuleRecord]:
    """Find modules matching criteria"""
    results = []
    
    # Search by keywords
    if criteria.keywords:
        results.extend(self.index.search_keywords(criteria.keywords))
    
    # Filter by type
    if criteria.type:
        results = [r for r in results if r.type == criteria.type]
    
    # Filter by compatibility
    if criteria.min_version:
        results = [r for r in results 
                  if self.version_compatible(r.version, criteria.min_version)]
    
    # Sort by relevance
    return self.rank_results(results, criteria)
```

### Dependency Resolution
```python
def resolve_dependencies(self, module_id: str) -> List[ModuleId]:
    """Get all dependencies for a module"""
    return self.dependency_graph.get_all_dependencies(module_id)

def check_conflicts(self, module_id: str) -> List[Conflict]:
    """Check for conflicts with loaded modules"""
    module = self.modules[module_id]
    conflicts = []
    
    for loaded_id in self.get_loaded_modules():
        loaded = self.modules[loaded_id]
        
        # Check explicit conflicts
        if self.has_conflict(module, loaded):
            conflicts.append(Conflict(module_id, loaded_id))
            
    return conflicts
```

## Module Index

Fast searching through module metadata:

```python
class ModuleIndex:
    """Inverted index for module search"""
    
    def __init__(self):
        self.keyword_index = {}  # keyword -> set of module_ids
        self.type_index = {}     # type -> set of module_ids
        self.tag_index = {}      # tag -> set of module_ids
        
    def search_keywords(self, keywords: List[str]) -> List[ModuleId]:
        """Find modules containing keywords"""
        results = set()
        
        for keyword in keywords:
            if keyword in self.keyword_index:
                results.update(self.keyword_index[keyword])
                
        return list(results)
```

## Dependency Graph

Manages module dependencies:

```python
class DependencyGraph:
    """Directed graph of module dependencies"""
    
    def __init__(self):
        self.graph = {}  # module_id -> set of dependencies
        self.reverse_graph = {}  # module_id -> set of dependents
        
    def get_all_dependencies(self, module_id: str) -> List[ModuleId]:
        """Get all transitive dependencies"""
        visited = set()
        queue = [module_id]
        
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
                
            visited.add(current)
            
            if current in self.graph:
                queue.extend(self.graph[current])
                
        visited.remove(module_id)  # Don't include self
        return list(visited)
```

## Version Management

```python
class VersionManager:
    """Handle semantic versioning"""
    
    def compatible(self, required: str, available: str) -> bool:
        """Check version compatibility"""
        req_major, req_minor, req_patch = self.parse_version(required)
        avail_major, avail_minor, avail_patch = self.parse_version(available)
        
        # Major version must match
        if req_major != avail_major:
            return False
            
        # Minor version must be >= required
        if avail_minor < req_minor:
            return False
            
        # If minor matches, patch must be >= required
        if avail_minor == req_minor and avail_patch < req_patch:
            return False
            
        return True
```

## Registry API

```python
# Registration
registry.register_module("path/to/module")
registry.unregister_module("module_id")
registry.update_module("module_id", "new/path")

# Discovery
registry.find_by_keyword("python")
registry.find_by_type(ModuleType.KNOWLEDGE)
registry.find_by_tags(["programming", "web"])

# Dependencies
registry.get_dependencies("module_id")
registry.get_dependents("module_id")
registry.check_conflicts("module_id")

# Stats
registry.get_stats("module_id")
registry.get_popular_modules(limit=10)
registry.get_recent_modules(days=7)
```

## Events

The registry emits these events:
- `module_registered` - New module added
- `module_updated` - Module updated
- `module_unregistered` - Module removed
- `index_updated` - Search index updated

## Configuration

```yaml
module_registry:
  max_modules: 10000
  index_update_interval: 60  # seconds
  validation_level: strict
  auto_cleanup: true
  cleanup_after_days: 90
```

## Next Steps

- See [Module Loader](module_loader.md) for loading modules
- See [Storage Tiers](storage_tiers.md) for storage details
- See [Module Validator](module_validator.md) for validation
