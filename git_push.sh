#!/bin/bash
# Simple push script after git init

echo "📤 Pushing to GitHub..."

# Test SSH connection first
echo "🔐 Testing SSH connection..."
ssh -T git@github.com 2>&1

# Push to origin
echo -e "\n🚀 Pushing to origin/main..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Success! Repository pushed to:"
    echo "   https://github.com/MikeyBeez/cortex_2"
else
    echo -e "\n❌ Push failed. Common issues:"
    echo "1. Repository not created on GitHub yet"
    echo "2. SSH key not set up"
    echo "3. Repository name mismatch"
fi
