# UV Package Management

Cortex_2 uses `uv` for all Python package management. This document explains our setup and best practices.

## Why UV?

- **Fast**: 10-100x faster than pip
- **Reliable**: Better dependency resolution
- **Simple**: Drop-in pip replacement
- **Modern**: Built for contemporary Python development

## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with Homebrew
brew install uv
```

## Basic Usage

### Create Virtual Environment
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies
```bash
# Install from pyproject.toml
uv pip install -e .

# Install with dev dependencies
uv pip install -e ".[dev]"

# Install specific package
uv pip install fastapi

# Install from requirements.txt
uv pip install -r requirements.txt
```

### Manage Dependencies
```bash
# Show installed packages
uv pip list

# Show package info
uv pip show fastapi

# Uninstall package
uv pip uninstall fastapi
```

## Cortex-Specific Setup

### Development Environment
```bash
# Full development setup
./setup.sh

# Or manually:
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Production Environment
```bash
uv venv --python 3.11
source .venv/bin/activate
uv pip install -e .
```

### Testing Environment
```bash
uv venv test-env
source test-env/bin/activate
uv pip install -e ".[dev]"
pytest
```

## Best Practices

### 1. Always Use UV
Never use regular pip in Cortex projects:
```bash
# ❌ Don't do this
pip install package

# ✅ Do this
uv pip install package
```

### 2. Lock Dependencies
Create reproducible environments:
```bash
# Generate lock file
uv pip freeze > requirements-lock.txt

# Install from lock file
uv pip install -r requirements-lock.txt
```

### 3. Multiple Environments
Keep environments separate:
```bash
# Development
uv venv dev-env

# Testing
uv venv test-env

# Benchmarking
uv venv bench-env
```

### 4. Python Version
Specify Python version explicitly:
```bash
uv venv --python 3.11
```

## Module Development

When creating new modules with dependencies:

```python
# In module's requirements.txt
numpy>=1.24
pandas>=2.0
scikit-learn>=1.3
```

Install for module development:
```bash
cd modules/my_module
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Troubleshooting

### UV Not Found
```bash
# Add to PATH
export PATH="$HOME/.cargo/bin:$PATH"

# Or reinstall
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Permission Issues
```bash
# Install for current user
curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --no-modify-path
```

### Cache Issues
```bash
# Clear UV cache
uv clean
```

## Integration with IDEs

### VS Code
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.terminal.activateEnvironment": true
}
```

### PyCharm
1. Settings → Project → Python Interpreter
2. Add Interpreter → Existing Environment
3. Select `.venv/bin/python`

## CI/CD Integration

### GitHub Actions
```yaml
- name: Install UV
  uses: astral-sh/setup-uv@v2
  
- name: Create venv and install
  run: |
    uv venv
    source .venv/bin/activate
    uv pip install -e ".[dev]"
    pytest
```

## Performance Tips

1. **Use System Python**: `uv venv --system-site-packages`
2. **Parallel Installation**: UV does this automatically
3. **Cache Reuse**: UV caches aggressively
4. **Minimal Reinstalls**: UV only reinstalls what changed

## Future UV Features

Planned Cortex integrations:
- Module dependency resolution via UV
- UV-based module packaging
- Automated environment switching
- UV workspace support

---

Remember: **Always use UV for Cortex development!** 🚀
