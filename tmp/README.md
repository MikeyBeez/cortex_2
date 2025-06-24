# /Users/bard/Code/cortex_2/tmp/README.md
# Temporary Files Directory

This directory contains all temporary, experimental, and one-off files that are NOT part of the core Cortex_2 system.

## What Goes Here

- Test scripts (`test_*.py`)
- Migration scripts (`migrate_*.py`)
- Experimental code (`experiment_*.py`)
- One-off fixes (`fix_*.py`)
- Data processing scripts
- Temporary reports
- Proof of concepts
- Any file you need to run but don't want in the core codebase

## Important Notes

1. **Files here are NOT part of Cortex_2 core**
2. **Files may be deleted at any time**
3. **Do NOT import from these files in core code**
4. **Use for development and testing only**

## Why This Exists

To keep the core Cortex_2 codebase minimal and clean. Every file in the core directories potentially uses context window space, so we keep only essential code there.

## Git Policy

Most files in this directory are ignored by git (see .gitignore). If you need to keep something, move it to the appropriate core directory.
