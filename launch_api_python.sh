#!/bin/bash
# Alternative launch script using Python directly

# Set up environment
export PYTHONUNBUFFERED=1
export PYTHONPATH="/Users/bard/Code/cortex_2/src"

# Change to project directory
cd /Users/bard/Code/cortex_2

# Activate virtual environment if it exists
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Run uvicorn directly with Python
exec python -m uvicorn cortex.app:app --host 0.0.0.0 --port 8000
