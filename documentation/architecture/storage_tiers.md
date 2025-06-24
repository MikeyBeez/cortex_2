# Storage Tiers

Cortex_2 uses a three-tier storage system to optimize memory usage and access speed. Modules move between tiers based on usage patterns.

## Overview

```
┌─────────────┐
│ HOT Storage │ ← Active modules (instant access)
├─────────────┤
│WARM Storage │ ← Recent modules (fast access)
├─────────────┤
│COLD Storage │ ← Archived modules (slow access)
└─────────────┘
```

## Hot Storage (Active Memory)

### Characteristics
- Uncompressed modules in RAM
- Instant access (0-5ms)
- Limited by memory budget
- Full functionality available

### Implementation
```python
class HotStorage:
    """Active module storage"""
    
    def __init__(self, max_size: int):
        self.modules = {}  # module_id -> Module
        self.max_size = max_size
        self.current_size = 0
        
    def store(self, module: Module) -> bool:
        """Store module in hot storage"""
        if self.current_size + module.size > self.max_size:
            return False
            
        self.modules[module.id] = module
        self.current_size += module.size
        return True
        
    def retrieve(self, module_id: str) -> Module:
        """Get module instantly"""
        return self.modules.get(module_id)
```

## Warm Storage

### Characteristics
- Lightly compressed (2-3x)
- Fast access (50-100ms)
- Memory-mapped files
- Quick decompression

### Implementation
```python
class WarmStorage:
    """Recently used module storage"""
    
    def __init__(self, storage_dir: Path):
        self.storage_dir = storage_dir
        self.index = {}  # module_id -> file_location
        
    def store(self, module: Module) -> None:
        """Compress and store module"""
        # Light compression
        compressed = self.light_compress(module)
        
        # Write to memory-mapped file
        file_path = self.storage_dir / f"{module.id}.warm"
        with mmap_write(file_path) as mm:
            mm.write(compressed)
            
        # Update index
        self.index[module.id] = file_path
        
    def retrieve(self, module_id: str) -> Module:
        """Load and decompress module"""
        file_path = self.index[module_id]
        
        # Memory-mapped read
        with mmap_read(file_path) as mm:
            compressed = mm.read()
            
        # Fast decompression
        return self.light_decompress(compressed)
```

### Compression Strategy
```python
def light_compress(self, module: Module) -> bytes:
    """Fast compression for warm storage"""
    # Remove whitespace and comments
    minified = self.minify(module.content)
    
    # Use fast compression algorithm
    return lz4.compress(minified, acceleration=True)
```

## Cold Storage

### Characteristics
- Heavily compressed (10x+)
- Slow access (1-5s)
- Disk-based storage
- Maximum compression

### Implementation
```python
class ColdStorage:
    """Long-term module archive"""
    
    def __init__(self, archive_dir: Path):
        self.archive_dir = archive_dir
        self.catalog = self.load_catalog()
        
    def archive(self, module: Module) -> None:
        """Heavily compress and archive"""
        # Maximum compression
        compressed = self.heavy_compress(module)
        
        # Write to disk
        archive_path = self.archive_dir / f"{module.id}.cold"
        with open(archive_path, 'wb') as f:
            f.write(compressed)
            
        # Update catalog
        self.catalog[module.id] = {
            'path': archive_path,
            'compressed_size': len(compressed),
            'compression_ratio': module.size / len(compressed)
        }
        
    def retrieve(self, module_id: str) -> Module:
        """Retrieve from archive"""
        info = self.catalog[module_id]
        
        # Read from disk
        with open(info['path'], 'rb') as f:
            compressed = f.read()
            
        # Decompress
        return self.heavy_decompress(compressed)
```

### Compression Strategy
```python
def heavy_compress(self, module: Module) -> bytes:
    """Maximum compression for cold storage"""
    # Extract essential content only
    essential = self.extract_essential(module)
    
    # Use best compression
    return lzma.compress(
        essential,
        preset=9,  # Maximum compression
        check=lzma.CHECK_CRC64
    )
```

## Tier Management

### Movement Between Tiers
```python
class TierManager:
    """Manage module movement between tiers"""
    
    def promote(self, module_id: str, from_tier: Tier, to_tier: Tier):
        """Move module to higher tier"""
        # Retrieve from current tier
        module = from_tier.retrieve(module_id)
        
        # Store in new tier
        if to_tier == Tier.HOT:
            # May need to evict others first
            self.ensure_space(module.size)
            
        to_tier.store(module)
        
        # Remove from old tier
        from_tier.remove(module_id)
        
    def demote(self, module_id: str, from_tier: Tier, to_tier: Tier):
        """Move module to lower tier"""
        module = from_tier.retrieve(module_id)
        
        # Compress appropriately
        if to_tier == Tier.WARM:
            compressed = self.light_compress(module)
        else:  # COLD
            compressed = self.heavy_compress(module)
            
        to_tier.store_compressed(module_id, compressed)
        from_tier.remove(module_id)
```

### Eviction Policies
```python
class EvictionPolicy:
    """Decide what to evict"""
    
    def select_for_eviction(self, needed_space: int) -> List[str]:
        """Select modules to evict"""
        candidates = self.get_eviction_candidates()
        
        # Score each candidate
        scored = []
        for module_id in candidates:
            score = self.calculate_eviction_score(module_id)
            scored.append((score, module_id))
            
        # Sort by score (higher = more likely to evict)
        scored.sort(reverse=True)
        
        # Select enough to free space
        to_evict = []
        freed_space = 0
        
        for score, module_id in scored:
            to_evict.append(module_id)
            freed_space += self.get_module_size(module_id)
            
            if freed_space >= needed_space:
                break
                
        return to_evict
```

## Access Patterns

### Predictive Loading
```python
def predict_access(self, context: Context) -> List[str]:
    """Predict which modules will be needed"""
    predictions = []
    
    # Time-based predictions
    hour = datetime.now().hour
    predictions.extend(self.time_based_predictions[hour])
    
    # Context-based predictions
    for keyword in context.keywords:
        predictions.extend(self.keyword_predictions.get(keyword, []))
        
    # Sequential predictions
    if self.last_loaded:
        predictions.extend(self.sequence_predictions.get(self.last_loaded, []))
        
    return predictions
```

## Performance Optimization

### Caching
```python
class TierCache:
    """Cache frequently accessed modules"""
    
    def __init__(self, cache_size: int):
        self.cache = LRUCache(cache_size)
        
    def get(self, module_id: str) -> Optional[Module]:
        """Try cache first"""
        return self.cache.get(module_id)
        
    def put(self, module_id: str, module: Module):
        """Cache for future access"""
        self.cache.put(module_id, module)
```

### Batch Operations
```python
def batch_promote(self, module_ids: List[str], to_tier: Tier):
    """Promote multiple modules efficiently"""
    # Load all in parallel
    modules = self.parallel_load(module_ids)
    
    # Ensure space for all
    total_size = sum(m.size for m in modules)
    self.ensure_space(total_size)
    
    # Store all
    for module in modules:
        to_tier.store(module)
```

## Configuration

```yaml
storage_tiers:
  hot:
    max_size: 50000  # tokens
    eviction_policy: "lru"
    
  warm:
    directory: "storage/warm"
    max_modules: 100
    compression: "lz4"
    
  cold:
    directory: "storage/cold"
    compression: "lzma"
    compression_level: 9
    
  promotion_threshold: 5  # uses
  demotion_threshold: 3600  # seconds
```

## Monitoring

```python
# Get storage statistics
stats = cortex.storage.get_stats()
print(f"Hot: {stats.hot.count} modules, {stats.hot.size} tokens")
print(f"Warm: {stats.warm.count} modules, {stats.warm.size_mb} MB")
print(f"Cold: {stats.cold.count} modules, {stats.cold.size_gb} GB")

# Monitor tier movements
cortex.storage.on("tier_change", lambda e: 
    print(f"{e.module_id}: {e.from_tier} → {e.to_tier}")
)
```

## Next Steps

- See [Resource Monitor](resource_monitor.md) for memory management
- See [Module Loader](module_loader.md) for loading details
- See [Eviction Strategies](eviction_strategies.md) for policies
