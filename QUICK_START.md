# Cortex_2 Quick Start Guide

Get started with Cortex_2 in minutes!

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mikeybee/cortex_2
cd cortex_2
```

### 2. Set Up Python Environment with UV
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run the setup script
./setup.sh
# Or if you get permission denied:
chmod +x setup.sh && ./setup.sh
```

### 3. Using UV Commands

With UV, you don't need to activate the virtual environment. Instead, use `uv run`:

```bash
# Run any Python command
uv run python --version

# Run the CLI
uv run python -m cortex.cli

# Run tests
uv run pytest

# Or use the Makefile shortcuts
make test
make test-quick
```

### 4. Add to Claude Code
```bash
claude mcp add cortex -s user -- node /path/to/cortex_2/mcp_server/dist/index.js
```

## Basic Usage

### Load Your First Module
```
You: "I need help with Python code"
Claude: [Uses Cortex to analyze context]
> analyze_context("I need help with Python code")
> load_module("python_expertise")
Claude: "I've loaded the Python expertise module. How can I help with your code?"
```

### Switch Personas
```
You: "Let's work on creative writing"
Claude: [Switches to creative mode]
> apply_persona("creative_writer")
> unload_module("python_expertise")
> load_module("creative_writing")
Claude: "I've switched to creative writing mode. What story shall we create?"
```

### Monitor Resources
```
You: "Check memory usage"
Claude: [Checks system resources]
> get_memory_usage()
Claude: "Using 75,000 of 100,000 tokens. Main modules loaded: python_expertise (50k), debugging_tools (20k)"
```

## Development Commands

```bash
# Run tests
make test              # All tests
make test-quick        # Quick unit tests
make test-cov          # With coverage

# Code quality
make lint              # Run linting
make format            # Format code

# Development
make dev               # Start dev server
make docs              # Serve documentation

# Module management
make module-create     # Create new module
make module-list       # List modules
make module-test       # Test a module

# Run any command with uv
make run python --version
make run pytest -v tests/unit/test_event_bus.py
```

## Creating Your First Module

### 1. Create Module Structure
```bash
mkdir -p modules/my_module/{content,triggers}
```

### 2. Create Manifest
```yaml
# modules/my_module/manifest.yaml
id: my_module
version: 1.0.0
type: knowledge
metadata:
  name: My Custom Module
  description: My domain expertise
  size_tokens: 10000
triggers:
  keywords: [myterm, mydomain]
content:
  knowledge_files:
    - content/knowledge.json
```

### 3. Add Knowledge
```json
// modules/my_module/content/knowledge.json
{
  "concepts": {
    "myterm": "Definition and explanation",
    "mydomain": "Domain-specific knowledge"
  },
  "examples": [
    "Example usage 1",
    "Example usage 2"
  ]
}
```

### 4. Register Module
```bash
uv run python -m cortex module register modules/my_module
```

## Common Workflows

### Programming Session
1. Start with base identity
2. Context detection loads programming modules
3. As you switch between languages, modules swap
4. Debugging tools load when needed

### Creative Writing
1. Apply creative persona
2. Load writing modules
3. Grammar and style modules activate
4. Technical modules unload to save memory

### Learning Mode
1. Load teaching persona
2. Explanation modules activate
3. Example generation tools load
4. Complexity adapts to understanding

## Tips and Tricks

### 1. Use UV Run
Always use `uv run` instead of activating the venv:
```bash
# Instead of: source .venv/bin/activate && python script.py
uv run python script.py
```

### 2. Let Context Drive Loading
Don't manually load modules unless needed. Cortex learns your patterns.

### 3. Use Personas for Context Switching
Personas automatically load appropriate modules.

### 4. Monitor Memory Usage
Keep an eye on memory to ensure smooth operation.

### 5. Provide Feedback
Help Cortex learn by providing feedback on what worked.

## Troubleshooting

### Module Won't Load
- Check if module exists: `uv run python -m cortex module list`
- Verify dependencies are loaded
- Check memory availability

### High Memory Usage
- Run `optimize_memory()` to free space
- Unload unnecessary modules
- Check for memory leaks

### UV Issues
- Make sure UV is in your PATH
- Update UV: `uv self update`
- Check UV version: `uv --version`

## Next Steps

1. Explore available modules
2. Create custom modules for your work
3. Train Cortex on your patterns
4. Share modules with the community

Happy cognitive computing! 🧠
