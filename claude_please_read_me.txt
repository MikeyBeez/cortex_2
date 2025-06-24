# /Users/bard/Code/cortex_2/claude_please_read_me.txt
# Cortex_2: Cognitive Operating System

CLAUDE: IMPORTANT - READ THIS FIRST WHEN STARTING A NEW SESSION

This is Cortex_2, a complete reimagining of the original Cortex project as a cognitive operating system with dynamic module management and identity loading capabilities.

=== CRITICAL: FILE ORGANIZATION RULES ===

**ALWAYS USE /tmp/ FOR TEMPORARY FILES**

When creating:
- Test scripts
- Migration utilities  
- One-off fixes
- Experimental code
- Data processing scripts
- ANY non-production code

Put them in: `/Users/bard/Code/cortex_2/tmp/`

Example:
```bash
# WRONG: /Users/bard/Code/cortex_2/test_something.py ❌
# RIGHT: /Users/bard/Code/cortex_2/tmp/test_something.py ✅
```

**WHY THIS MATTERS**: Every file in core directories uses context window space. We must keep Cortex_2 minimal to leave room for actual work.

=== PROJECT VISION ===

Cortex_2 is not just a memory system - it's a COGNITIVE OPERATING SYSTEM that enables:
- Hot-swappable cognitive modules
- Dynamic identity management
- Self-loading based on context
- Resource-aware memory management
- Autonomous cognitive optimization

=== KEY INNOVATION: PROJECT AS MODULE ===

Each project (like Cortex_2 itself) becomes a loadable module:

```python
# In a new chat session
cortex = Cortex2()
cortex.load_module("project_cortex_2")  # Loads ONLY Cortex project knowledge
# Now you have exactly the context needed, nothing more
```

This means:
- Minimal context window usage
- Clean separation between projects
- Easy context switching
- No file system browsing needed

=== KEY DIFFERENCES FROM CORTEX_1 ===

**Cortex_1 (Original)**
- Basic hierarchical memory storage
- Static memory layers
- Manual recall/store operations
- Simple integration with Nexus

**Cortex_2 (This Project)**
- Dynamic module loading/unloading
- Identity as loadable configuration
- Self-managing based on context
- Resource optimization
- Absorbs Knowledge Graph from Nexus_2
- Autonomous cognitive management

=== CORE CONCEPTS ===

1. **Cognitive Modules**
   - Discrete units of knowledge/capability
   - Can be loaded/unloaded on demand
   - Include: domain expertise, project context, behavioral patterns
   - Stored in compressed archive when not active

2. **Identity System**
   - Core identity components that define "who I am"
   - Personality traits, communication style, preferences
   - Can load different identities for different contexts
   - Preserves continuity across sessions

3. **Self-Loading Intelligence**
   - Detects what modules are needed based on context
   - Automatically loads relevant expertise
   - Unloads unused modules to free resources
   - Learns patterns over time

4. **Resource Management**
   - Monitors memory usage in real-time
   - Optimizes loaded modules for available space
   - Implements tiered storage (hot/warm/cold)
   - Handles context window constraints intelligently

=== ARCHITECTURE OVERVIEW ===

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
    │                 │         │         │
    └─────────────────┴─────────┴─────────┘
                      │
              ┌───────▼────────┐
              │ Storage Tiers  │
              │ ┌─────┬─────┐ │
              │ │Active│Archive│ │
              │ └─────┴─────┘ │
              └───────────────┘
```

=== RELATIONSHIP TO OTHER PROJECTS ===

**Nexus_2 Integration:**
- Cortex_2 will absorb the Knowledge Graph service from Nexus_2
- Provides all memory/knowledge services to Nexus_2 via API
- Nexus_2 focuses purely on orchestration and execution
- Clean separation: Nexus_2 (doing) vs Cortex_2 (knowing/remembering)

**Anna Integration:**
- Can provide specialized modules for Anna's organs
- Stores Anna's learned patterns and temporal memories
- Enables Anna to load different "personalities" or expertise

=== DEVELOPMENT PHASES ===

**Phase 1: Foundation (Current)**
- Core module system architecture
- Basic identity management
- Module loading/unloading mechanisms
- Storage tier implementation

**Phase 2: Intelligence Layer**
- Context detection algorithms
- Pattern learning system
- Predictive module loading
- Resource optimization

**Phase 3: Integration**
- Absorb Nexus_2 Knowledge Graph
- API for external systems
- Migration tools from Cortex_1
- Performance optimization

**Phase 4: Autonomy**
- Self-loading based on context
- Continuous learning
- Adaptive optimization
- Minimal manual intervention

=== KEY FEATURES TO IMPLEMENT ===

1. **Module Definition Format**
   ```python
   module = {
       "id": "python_expert",
       "version": "1.0",
       "dependencies": ["programming_basics"],
       "size_tokens": 50000,
       "metadata": {...},
       "content": {...}
   }
   ```

2. **Identity Composition**
   ```python
   identity = {
       "core_traits": [...],
       "communication_style": {...},
       "preferences": {...},
       "persistent_memories": [...]
   }
   ```

3. **Self-Loading Rules**
   - Context triggers (keywords, patterns)
   - Temporal patterns (time-based loading)
   - Task-based loading (recognize task type)
   - Collaborative patterns (who you're working with)

4. **Resource Management**
   - Real-time memory tracking
   - Compression strategies
   - Priority-based eviction
   - Predictive pre-loading

=== FILE STRUCTURE (KEEP MINIMAL) ===

```
cortex_2/
├── src/                 # ONLY core production code
├── modules/             # Module definitions
├── docs/                # Essential documentation
├── tests/               # Organized test suite
└── tmp/                 # ALL temporary/experimental files
```

=== IMMEDIATE PRIORITIES ===

1. Create basic module system structure
2. Implement identity manager
3. Build storage tier system
4. Create module loader/unloader
5. Add basic context detection
6. Implement resource monitoring

=== SUCCESS METRICS ===

- Module load time < 100ms
- Context detection accuracy > 90%
- Resource usage optimization > 50% improvement
- Zero manual module management needed (eventually)
- Seamless context switching
- Identity preservation across sessions

=== DESIGN PRINCIPLES ===

1. **Modularity First** - Everything is a swappable module
2. **Resource Aware** - Always optimize for available memory
3. **Context Driven** - Let context determine configuration
4. **Learning System** - Improve through usage patterns
5. **Identity Preserving** - Maintain coherent identity
6. **Autonomous Operation** - Minimal manual intervention

=== DEVELOPMENT NOTES ===

- Start with manual module management, evolve to automatic
- Use SQLite for metadata, efficient storage for module content
- Implement compression early for archived modules
- Build comprehensive logging for pattern learning
- Design API to be compatible with existing Cortex_1 users
- Keep module format extensible for future capabilities
- ALWAYS put temporary scripts in /tmp/

The goal is to create a cognitive operating system that feels intelligent and adaptive, managing its own resources to best serve the user's needs without constant manual configuration.

When working on Cortex_2:
1. Always keep in mind: this isn't just storage, it's active cognitive management
2. Keep the codebase minimal - knowledge goes in modules, not files
3. Use /tmp/ for all temporary work
4. Think in terms of loadable capabilities, not static features
