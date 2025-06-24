# /Users/bard/Code/cortex_2/MIGRATION_FROM_CORTEX.md
# Migration Guide: Cortex → Cortex_2

This guide helps you migrate from the original Cortex memory system to Cortex_2's cognitive operating system.

## Key Differences

### Cortex (Original)
- Static memory layers
- Manual store/recall operations  
- Fixed hierarchical structure
- Simple API focused on storage

### Cortex_2 (New)
- Dynamic module system
- Self-loading intelligence
- Identity management
- Resource optimization
- Cognitive operating system

## Migration Strategy

### Phase 1: Assessment

1. **Inventory Current Usage**
   ```python
   # Export your Cortex data
   from cortex import Cortex
   
   old_cortex = Cortex()
   
   # Export memories
   memories = old_cortex.export_all_memories()
   
   # Export configuration
   config = old_cortex.export_config()
   ```

2. **Identify Memory Types**
   - Session memories → Convert to working memory module
   - Episodic memories → Convert to context modules
   - Semantic memories → Convert to knowledge modules
   - Meta memories → Convert to pattern modules

### Phase 2: Data Conversion

#### Memory to Module Conversion

```python
from cortex2.migration import MemoryToModuleConverter

converter = MemoryToModuleConverter()

# Convert semantic memories to knowledge modules
for memory in semantic_memories:
    module = converter.convert_semantic_memory(memory)
    module.save(f"modules/{module.id}")

# Convert episodic memories to context modules  
for conversation in episodic_memories:
    module = converter.convert_conversation(conversation)
    module.save(f"modules/contexts/{module.id}")
```

#### Create Identity Modules

```python
# Extract identity patterns from memories
identity_extractor = IdentityExtractor()
identity = identity_extractor.analyze_memories(all_memories)

# Create identity module
identity_module = {
    "id": "migrated_identity",
    "metadata": {
        "source": "cortex_v1",
        "migration_date": datetime.now()
    },
    "components": {
        "traits": identity.traits,
        "communication_style": identity.style,
        "preferences": identity.preferences
    }
}
```

### Phase 3: Module Creation

#### Knowledge Graph → Knowledge Modules

The Knowledge Graph from Nexus_2 becomes part of Cortex_2:

```python
# Migrate knowledge graph
from cortex2.migration import KnowledgeGraphMigrator

migrator = KnowledgeGraphMigrator()

# Convert graph nodes to modules
for node_type in graph.get_node_types():
    module = migrator.create_module_from_nodes(
        node_type,
        graph.get_nodes_by_type(node_type)
    )
    module.save()
```

#### Project-Specific Modules

Convert project contexts into loadable modules:

```python
# Create project modules from memories
project_analyzer = ProjectAnalyzer()

for project in project_analyzer.detect_projects(memories):
    module = {
        "id": f"project_{project.name}",
        "content": {
            "context": project.context,
            "files": project.files,
            "patterns": project.patterns
        },
        "triggers": {
            "keywords": project.keywords,
            "paths": project.paths
        }
    }
```

### Phase 4: API Migration

#### Old Cortex API

```python
# Old way
cortex = Cortex()
cortex.store("Python info", memory_type="semantic")
memories = cortex.recall("python", limit=10)
```

#### New Cortex_2 API

```python
# New way - automatic
cortex2 = Cortex2()
cortex2.enable_self_loading()

# Cortex_2 automatically loads python_expertise module
response = cortex2.process("Tell me about Python")

# Or manual control
cortex2.load_module("python_expertise")
```

#### API Compatibility Layer

For gradual migration:

```python
from cortex2.compat import CortexCompatibility

# Drop-in replacement
cortex = CortexCompatibility()

# Old API works but uses new system
cortex.store("Information", memory_type="semantic")  # Creates module
cortex.recall("query")  # Searches loaded modules
```

### Phase 5: Integration Updates

#### Update Nexus_2 Integration

```python
# Old: Nexus_2 → Cortex
nexus_config = {
    "memory_system": {
        "type": "cortex",
        "endpoint": "http://localhost:8100"
    }
}

# New: Nexus_2 → Cortex_2
nexus_config = {
    "memory_system": {
        "type": "cortex2",
        "endpoint": "http://localhost:8200",
        "features": {
            "auto_loading": true,
            "identity": "nexus_assistant"
        }
    }
}
```

## Migration Script

Complete migration script:

```python
#!/usr/bin/env python3
"""
Migrate from Cortex to Cortex_2
"""

import json
from pathlib import Path
from datetime import datetime

from cortex import Cortex
from cortex2 import Cortex2
from cortex2.migration import MigrationManager

def migrate_cortex_to_cortex2(
    old_db_path: str = "cortex.db",
    new_config_path: str = "cortex2/config"
):
    """Complete migration from Cortex to Cortex_2"""
    
    print("🔄 Starting Cortex → Cortex_2 migration...")
    
    # Step 1: Export from old Cortex
    print("📤 Exporting from Cortex v1...")
    old_cortex = Cortex(database_path=old_db_path)
    
    export_data = {
        "metadata": {
            "export_date": datetime.now().isoformat(),
            "source_version": "cortex_v1",
            "total_memories": 0
        },
        "memories": {
            "session": [],
            "episodic": [],
            "semantic": [],
            "meta": []
        },
        "configuration": {}
    }
    
    # Export each memory type
    for memory_type in ["session", "episodic", "semantic", "meta"]:
        memories = old_cortex.get_memories_by_type(memory_type)
        export_data["memories"][memory_type] = memories
        export_data["metadata"]["total_memories"] += len(memories)
    
    # Step 2: Convert to modules
    print("🔄 Converting memories to modules...")
    manager = MigrationManager()
    
    modules_created = []
    
    # Convert semantic memories to knowledge modules
    for memory in export_data["memories"]["semantic"]:
        module = manager.semantic_to_module(memory)
        modules_created.append(module)
    
    # Convert episodic memories to context modules
    conversations = manager.group_episodic_memories(
        export_data["memories"]["episodic"]
    )
    
    for conv_id, memories in conversations.items():
        module = manager.conversation_to_module(conv_id, memories)
        modules_created.append(module)
    
    # Create identity from patterns
    identity = manager.extract_identity(export_data["memories"])
    if identity:
        modules_created.append(identity)
    
    # Step 3: Initialize Cortex_2
    print("🚀 Initializing Cortex_2...")
    cortex2 = Cortex2()
    
    # Step 4: Install modules
    print("📥 Installing modules...")
    for module in modules_created:
        cortex2.install_module(module)
        print(f"  ✓ Installed: {module['id']}")
    
    # Step 5: Verify migration
    print("✅ Verifying migration...")
    stats = cortex2.get_statistics()
    
    print(f"""
Migration Complete!
  Original memories: {export_data['metadata']['total_memories']}
  Modules created: {len(modules_created)}
  Total module size: {stats['total_size_tokens']} tokens
  
Next steps:
1. Test the migrated modules
2. Enable self-loading: cortex2.enable_self_loading()
3. Update integrations to use Cortex_2 API
    """)
    
    # Save migration report
    report_path = Path(new_config_path) / "migration_report.json"
    with open(report_path, 'w') as f:
        json.dump({
            "migration_date": datetime.now().isoformat(),
            "source_memories": export_data['metadata']['total_memories'],
            "modules_created": [m['id'] for m in modules_created],
            "verification": stats
        }, f, indent=2)
    
    return True

if __name__ == "__main__":
    migrate_cortex_to_cortex2()
```

## Testing Migration

### Verify Module Loading

```python
# Test that old memories are accessible
cortex2 = Cortex2()

# Should auto-load relevant modules
response = cortex2.process("What do you remember about Project X?")

# Verify specific modules
loaded = cortex2.list_loaded_modules()
assert "project_x_context" in loaded
```

### Compare Outputs

```python
# Old Cortex
old_memories = old_cortex.recall("python debugging")

# New Cortex_2  
cortex2.process("python debugging")
new_response = cortex2.get_last_response()

# Verify similar content retrieved
verify_migration_quality(old_memories, new_response)
```

## Rollback Plan

If issues arise:

1. **Keep Old System Running**
   - Don't delete Cortex v1 immediately
   - Run both systems in parallel initially

2. **Export Backup**
   ```bash
   cortex2 export --all --format=backup
   ```

3. **Rollback Procedure**
   ```python
   # Disable Cortex_2
   cortex2.disable()
   
   # Re-enable Cortex v1
   old_cortex.enable()
   
   # Update integrations to point back
   ```

## Common Issues

### Issue: Memory Size Explosion

**Problem**: Modules are too large after conversion
**Solution**: 
```python
# Use compression during migration
manager = MigrationManager(compress=True, max_module_size=50000)
```

### Issue: Missing Memories

**Problem**: Some memories don't appear in Cortex_2
**Solution**: Check module triggers
```python
# Debug triggers
cortex2.debug_triggers("query that should work")
```

### Issue: Performance Degradation

**Problem**: Cortex_2 slower than original
**Solution**: Optimize module loading
```python
# Pre-load common modules
cortex2.set_preload_modules(["common_knowledge", "base_identity"])
```

## Benefits After Migration

1. **Dynamic Loading**: Only load what you need
2. **Identity Management**: Switch between contexts easily
3. **Better Organization**: Modular structure
4. **Self-Optimization**: System learns your patterns
5. **Resource Efficiency**: Better memory management

---

*Migration is a one-time investment that unlocks the full power of Cortex_2's cognitive operating system.*
