#!/bin/bash
# Initialize and push Cortex_2 to private GitHub repo

echo "🚀 Setting up Cortex_2 GitHub repository"
echo "========================================"

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ] || [ ! -d "src/cortex" ]; then
    echo "❌ Error: Not in Cortex_2 directory!"
    echo "Please run from /Users/bard/Code/cortex_2"
    exit 1
fi

# 1. Check for existing .git directory
if [ -d ".git" ]; then
    echo "⚠️  Git repository already initialized"
    echo "Do you want to remove it and start fresh? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        rm -rf .git
        echo "✅ Removed existing .git directory"
    else
        echo "Keeping existing git setup"
    fi
else
    echo "✅ No existing git repository found"
fi

# 2. Initialize git repository
echo -e "\n📁 Initializing git repository..."
git init

# 3. Create comprehensive .gitignore
echo -e "\n📝 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.tox/
.mypy_cache/
.ruff_cache/

# Virtual Environment
.venv/
venv/
ENV/
env/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~
.DS_Store

# Logs
logs/*.log
*.log

# Temporary files
tmp/*.py
tmp/*.sh
tmp/*.log
tmp/*
!tmp/README.md

# Node modules (for MCP server)
node_modules/
mcp_server/node_modules/
mcp_server/dist/

# Environment files
.env
.env.local
.env.*.local

# macOS
.DS_Store
.AppleDouble
.LSOverride

# Credentials
*.pem
*.key
*_rsa
*_rsa.pub

# Database
*.db
*.sqlite
*.sqlite3

# Redis
dump.rdb

# Coverage reports
coverage.xml
*.cover

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# Secrets
secrets/
*.secret
EOF

# 4. Add all files
echo -e "\n📦 Adding files to git..."
git add .

# 5. Create initial commit
echo -e "\n💾 Creating initial commit..."
git commit -m "Initial commit: Cortex_2 - Cognitive Operating System

- FastAPI-based REST API with full OpenAPI documentation
- Knowledge Graph integration for cognitive capabilities
- Module system architecture for dynamic loading
- Identity management system structure
- Resource monitoring and optimization framework
- MCP (Model Context Protocol) server for Claude integration
- macOS service management via launchctl
- Comprehensive test suite structure
- Full documentation and API examples"

# 6. Set main branch
git branch -M main

# 7. Show instructions for GitHub
echo -e "\n📋 Next Steps:"
echo "=============="
echo ""
echo "1. Create a new PRIVATE repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: cortex_2"
echo "   - Select 'Private'"
echo "   - DO NOT initialize with README, .gitignore, or license"
echo "   - Click 'Create repository'"
echo ""
echo "2. After creating the repo, GitHub will show you commands."
echo "   Use these commands to push:"
echo ""
echo "   git remote add origin git@github.com:MikeyBeez/cortex_2.git"
echo "   git push -u origin main"
echo ""
echo "3. Verify your SSH key is set up:"
echo "   ssh -T git@github.com"
echo ""
echo "   You should see: 'Hi MikeyBeez! You've successfully authenticated...'"
echo ""
echo "4. If SSH isn't set up, see:"
echo "   https://docs.github.com/en/authentication/connecting-to-github-with-ssh"

# 8. Check current remotes
echo -e "\n📡 Current git remotes:"
git remote -v

# 9. Show git status
echo -e "\n📊 Git status:"
git status --short

echo -e "\n✅ Local repository is ready!"
echo "Now create the GitHub repo and push using the commands above."
