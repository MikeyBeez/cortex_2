# /Users/bard/Code/cortex_2/DEVELOPMENT_GUIDELINES.md
# Cortex_2 Development Guidelines

## CRITICAL: Code Organization Rules

### 1. Keep Core Code Minimal

**IMPORTANT**: Cortex_2 must remain lean to minimize context window usage. Follow these rules:

- **Core Code**: Only essential, production-ready code in the main directories
- **Temporary Files**: ALL test scripts, one-off utilities, and experimental code go in `/tmp/`
- **No Noise**: No abandoned scripts, test files, or experimental code in core directories

### 2. File Placement Rules

```
cortex_2/
├── src/                 # ONLY production code
│   ├── core/           # Core system components
│   ├── modules/        # Module system
│   └── api/            # API interfaces
├── modules/            # Module definitions ONLY
├── docs/               # Documentation ONLY
├── tests/              # Organized test suite ONLY
└── tmp/                # ALL temporary/experimental files
    ├── test_*.py       # One-off test scripts
    ├── migrate_*.py    # Migration scripts
    ├── experiment_*.py # Experimental code
    └── fix_*.py        # Temporary fixes
```

### 3. When to Use `/tmp/`

Put files in `/tmp/` when:
- Creating one-off scripts for testing
- Writing migration or transformation scripts
- Experimenting with new features
- Creating temporary fixes or patches
- Generating reports or analysis
- Building proof-of-concepts

Example:
```python
# WRONG: /Users/bard/Code/cortex_2/test_module_loading.py ❌
# RIGHT:  /Users/bard/Code/cortex_2/tmp/test_module_loading.py ✅
```

### 4. Clean Code Practices

- **No Debug Code**: Remove all print statements, debug code before committing
- **No Commented Code**: Delete, don't comment out
- **No Test Data**: Keep test data in tests/ or tmp/
- **No Personal Scripts**: Your personal utilities go in tmp/

### 5. Module Development

When creating modules, keep them minimal:

```yaml
# Module manifest should be concise
id: project_cortex_2
version: 1.0.0
content:
  knowledge:
    - architecture.json    # Essential architecture only
    - api.json            # Core API definitions only
triggers:
  keywords: [cortex, cognitive, module]
```

### 6. Context Window Optimization

Remember: Every file in the core directories potentially gets loaded into context.

**DO**:
- Keep files focused and single-purpose
- Use clear, minimal documentation
- Compress knowledge into modules
- Archive old code to `/tmp/` or remove

**DON'T**:
- Leave experimental code in src/
- Keep multiple versions of files
- Store large datasets in core directories
- Include verbose comments

### 7. Example: Creating a Migration Script

```bash
# Working on a migration script
cd /Users/bard/Code/cortex_2

# Create in tmp/
cat > tmp/migrate_cortex_v1_data.py << 'EOF'
#!/usr/bin/env python3
"""
Temporary migration script for Cortex v1 → v2
This will be run once and deleted
"""
# ... migration code ...
EOF

# Run it
python tmp/migrate_cortex_v1_data.py

# When done, either delete or archive
rm tmp/migrate_cortex_v1_data.py  # or keep for reference
```

### 8. Git Ignore Rules

The `.gitignore` includes:
```
# Ignore all tmp files by default
/tmp/*
# But allow README
!/tmp/README.md
# Allow specific files if needed
!/tmp/.gitkeep
```

### 9. Review Checklist

Before committing:
- [ ] Is this production code? → `src/`
- [ ] Is this a test? → `tests/`
- [ ] Is this documentation? → `docs/`
- [ ] Is this temporary? → `tmp/`
- [ ] Have I removed debug code?
- [ ] Is the file minimal and focused?

### 10. Module as Context

The vision: Each project becomes a loadable module that provides ONLY the needed context.

```python
# In a new chat session
cortex = Cortex2()

# Load only the Cortex project context
cortex.load_module("project_cortex_2")

# Now the session has:
# - Cortex architecture knowledge
# - API specifications
# - Development patterns
# - Nothing else!

# Start working with minimal context
response = cortex.process("What's the module loading sequence?")
```

## Why This Matters

1. **Context Efficiency**: Less code = more room for actual work
2. **Clarity**: Easy to find what matters
3. **Maintainability**: Clean codebase is easier to evolve
4. **Performance**: Faster loading, less to process
5. **Modularity**: Project knowledge as modules, not files

## Remember

> "The best code is no code. The second best is minimal code."

Cortex_2's power comes from its module system, not from having lots of files. Keep the core small, put knowledge in modules, and use `/tmp/` liberally for everything else.

---

*This is a living document. As Cortex_2 evolves, so will these guidelines.*
