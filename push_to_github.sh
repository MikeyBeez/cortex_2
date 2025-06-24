#!/bin/bash
# Push to GitHub after repo is created

echo "🚀 Pushing Cortex_2 to GitHub"
echo "============================"

# Check if remote exists
if git remote | grep -q "origin"; then
    echo "⚠️  Remote 'origin' already exists:"
    git remote -v
    echo ""
    echo "Do you want to remove it and set a new one? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        git remote remove origin
        echo "✅ Removed existing origin"
    fi
fi

# Add remote if it doesn't exist
if ! git remote | grep -q "origin"; then
    echo "Adding GitHub remote..."
    git remote add origin git@github.com:MikeyBeez/cortex_2.git
    echo "✅ Remote added"
fi

# Verify SSH connection
echo -e "\n🔐 Testing SSH connection to GitHub..."
ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"
if [ $? -eq 0 ]; then
    echo "✅ SSH authentication successful!"
else
    echo "❌ SSH authentication failed!"
    echo ""
    echo "To set up SSH keys:"
    echo "1. Generate a key: ssh-keygen -t ed25519 -C 'your_email@example.com'"
    echo "2. Start ssh-agent: eval \"\$(ssh-agent -s)\""
    echo "3. Add key: ssh-add ~/.ssh/id_ed25519"
    echo "4. Copy public key: pbcopy < ~/.ssh/id_ed25519.pub"
    echo "5. Add to GitHub: https://github.com/settings/keys"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Push to GitHub
echo -e "\n📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Successfully pushed to GitHub!"
    echo ""
    echo "🎉 Your repository is now at:"
    echo "   https://github.com/MikeyBeez/cortex_2"
    echo ""
    echo "📱 To clone on another machine:"
    echo "   git clone git@github.com:MikeyBeez/cortex_2.git"
else
    echo -e "\n❌ Push failed!"
    echo "Make sure you've created the repository on GitHub first."
fi
