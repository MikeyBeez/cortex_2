#!/bin/bash
# Clean up Cortex_2 project

echo "🧹 Cleaning up Cortex_2 project..."
echo "================================="

cd /Users/bard/Code/cortex_2

# 1. Remove all temporary test scripts
echo -e "\n1. Removing temporary files from /tmp/..."
rm -f tmp/test_*.py
rm -f tmp/test_*.sh
rm -f tmp/check_*.py
rm -f tmp/check_*.sh
rm -f tmp/fix_*.py
rm -f tmp/fix_*.sh
rm -f tmp/find_*.sh
rm -f tmp/restart_*.sh
rm -f tmp/reinstall_*.sh
rm -f tmp/run_*.py
rm -f tmp/simple_*.py
rm -f tmp/start_*.py
rm -f tmp/apply_*.sh
rm -f tmp/api_server.py
rm -f tmp/quick_*.py
rm -f tmp/*.sh
rm -f tmp/*.py

# 2. Clean up any backup files
echo -e "\n2. Removing backup files..."
find . -name "*.backup" -type f -delete
find . -name "*_backup.py" -type f -delete
find . -name "*_fixed.py" -type f -delete
find . -name "*_simple.py" -type f -delete

# 3. Clean up Python cache files
echo -e "\n3. Cleaning Python cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete

# 4. Clean up any .DS_Store files (macOS)
echo -e "\n4. Removing .DS_Store files..."
find . -name ".DS_Store" -type f -delete

# 5. Keep only essential files in tmp/
echo -e "\n5. Keeping tmp/ directory clean..."
# Keep the README if it exists
if [ ! -f tmp/README.md ]; then
    echo "# Temporary Files Directory" > tmp/README.md
    echo "" >> tmp/README.md
    echo "This directory is for temporary scripts and experiments." >> tmp/README.md
    echo "All files here should be considered disposable." >> tmp/README.md
fi

# 6. Update .gitignore to ensure tmp files aren't tracked
echo -e "\n6. Updating .gitignore..."
if ! grep -q "tmp/" .gitignore 2>/dev/null; then
    echo -e "\n# Temporary files" >> .gitignore
    echo "tmp/*.py" >> .gitignore
    echo "tmp/*.sh" >> .gitignore
    echo "tmp/*.log" >> .gitignore
fi

# 7. Clear old logs (keep last 100 lines)
echo -e "\n7. Trimming log files..."
if [ -f logs/cortex.log ]; then
    tail -100 logs/cortex.log > logs/cortex.log.tmp
    mv logs/cortex.log.tmp logs/cortex.log
fi
if [ -f logs/cortex-error.log ]; then
    tail -100 logs/cortex-error.log > logs/cortex-error.log.tmp
    mv logs/cortex-error.log.tmp logs/cortex-error.log
fi

# 8. List what remains in tmp/
echo -e "\n8. Contents of tmp/ after cleanup:"
ls -la tmp/ | grep -v "^total"

# 9. Show project structure
echo -e "\n9. Clean project structure:"
tree -L 2 -I '__pycache__|*.pyc|.git|.venv|node_modules' 2>/dev/null || {
    echo "Main directories:"
    ls -d */ | grep -v "__pycache__"
}

# 10. Summary
echo -e "\n✅ Cleanup Complete!"
echo "========================="
echo "- Removed all temporary test scripts"
echo "- Cleaned Python cache files"
echo "- Trimmed log files"
echo "- Updated .gitignore"
echo ""
echo "🚀 Cortex_2 is clean and ready!"
echo ""
echo "Key commands:"
echo "  make dev          - Start development server"
echo "  make test         - Run tests"
echo "  make service-status - Check service status"
echo "  make service-logs - View service logs"
echo ""
echo "API endpoints:"
echo "  http://localhost:8000       - API root"
echo "  http://localhost:8000/docs  - Interactive docs"
echo "  http://localhost:8000/redoc - ReDoc documentation"
