#!/bin/bash
# /Users/bard/Code/cortex_2/setup.sh

echo "🧠 Setting up Cortex_2 development environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Create virtual environment with uv
echo "🐍 Creating virtual environment with uv..."
uv venv

# Activate virtual environment
echo "✨ Activating environment..."
source .venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
uv pip install -e ".[dev]"

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p src/cortex/{core,modules,context,identity,resources,learning}
mkdir -p modules
mkdir -p tests/{unit,integration,system}
mkdir -p storage/{hot,warm,cold}
mkdir -p config

# Create initial config
echo "⚙️ Creating default configuration..."
cat > config/cortex.yaml << EOF
memory:
  limit: 100000
  buffer: 5000
  
storage:
  hot_size: 50000
  warm_directory: ./storage/warm
  cold_directory: ./storage/cold
  
learning:
  enabled: true
  exploration_rate: 0.1
  
identity:
  default: "assistant"
  auto_adapt: true
  
modules:
  auto_load: true
  search_paths:
    - ./modules
    - ~/.cortex/modules
EOF

# Build MCP server
echo "🔧 Building MCP server..."
cd mcp_server
npm install
npm run build
cd ..

# Create CLI entry point
echo "🚀 Creating CLI tool..."
mkdir -p src/cortex
cat > src/cortex/__init__.py << EOF
"""Cortex_2: Cognitive Operating System"""
__version__ = "0.1.0"
EOF

cat > src/cortex/cli.py << EOF
#!/usr/bin/env python3
"""Cortex CLI interface"""
import click

@click.group()
def cli():
    """Cortex_2 Cognitive Operating System"""
    pass

@cli.command()
def module():
    """Module management commands"""
    click.echo("Module commands coming soon...")

@cli.command()
def server():
    """Start Cortex server"""
    click.echo("Starting Cortex server...")

def main():
    cli()

if __name__ == "__main__":
    main()
EOF

# Make setup script executable
chmod +x setup.sh

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate environment: source .venv/bin/activate"
echo "2. Run tests: pytest"
echo "3. Start development: python -m cortex.cli"
echo "4. Add to Claude: claude mcp add cortex -s user -- node $(pwd)/mcp_server/dist/index.js"
