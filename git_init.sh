#!/bin/bash
# Initialize git and push to GitHub

echo "🚀 Initializing Cortex_2 Git Repository"
echo "======================================"

cd /Users/bard/Code/cortex_2

# 1. Check if already initialized
if [ -d ".git" ]; then
    echo "⚠️  Warning: .git directory already exists"
    echo "Remove it and start fresh? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        rm -rf .git
        echo "✅ Removed existing .git directory"
    else
        echo "❌ Aborted. Please handle existing git repo manually."
        exit 1
    fi
fi

# 2. Initialize git
echo -e "\n📁 Initializing git repository..."
git init

# 3. Add all files
echo -e "\n📦 Adding all files..."
git add .

# 4. Show what will be committed
echo -e "\n📋 Files to be committed:"
git status --short

# 5. Create initial commit
echo -e "\n💾 Creating initial commit..."
git commit -m "Initial commit: Cortex_2 - Cognitive Operating System

Features:
- FastAPI REST API with OpenAPI documentation
- Knowledge Graph integration for cognitive capabilities  
- Module system architecture for dynamic loading
- Identity management system structure
- Resource monitoring and optimization framework
- MCP (Model Context Protocol) server for Claude integration
- macOS service management via launchctl
- Comprehensive test suite structure

Tech stack:
- Python 3.10+ with FastAPI, Pydantic, PyYAML
- TypeScript/Node.js for MCP server
- SQLite/Redis for storage (planned)
- pytest for testing

Author: MikeyBee"

# 6. Add remote origin
echo -e "\n🔗 Adding remote origin..."
git remote add origin git@github.com:MikeyBeez/cortex_2.git

# 7. Rename branch to main
echo -e "\n🌿 Setting branch to main..."
git branch -M main

# 8. Show current setup
echo -e "\n📊 Current git configuration:"
echo "Repository: $(pwd)"
echo "Branch: $(git branch --show-current)"
echo "Remote:"
git remote -v

# 9. Ready to push
echo -e "\n✅ Ready to push!"
echo "===================================="
echo ""
echo "Make sure you've created the repository on GitHub:"
echo "1. Go to: https://github.com/new"
echo "2. Name: cortex_2"  
echo "3. Set as PRIVATE"
echo "4. DO NOT initialize with any files"
echo "5. Click 'Create repository'"
echo ""
echo "Then push with:"
echo "  git push -u origin main"
echo ""
echo "Or run: ./push_to_github.sh"
