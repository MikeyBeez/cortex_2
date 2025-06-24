#!/bin/bash
# Launch script for Cortex_2 API server

# Set up environment
export PYTHONUNBUFFERED=1
export PYTHONPATH="/Users/bard/Code/cortex_2/src"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

# Change to project directory
cd /Users/bard/Code/cortex_2

# Find uv executable
UV_PATH=$(which uv)
if [ -z "$UV_PATH" ]; then
    # Check common locations
    if [ -x "/opt/homebrew/bin/uv" ]; then
        UV_PATH="/opt/homebrew/bin/uv"
    elif [ -x "/usr/local/bin/uv" ]; then
        UV_PATH="/usr/local/bin/uv"
    elif [ -x "$HOME/.cargo/bin/uv" ]; then
        UV_PATH="$HOME/.cargo/bin/uv"
    else
        echo "Error: uv not found in PATH" >&2
        exit 1
    fi
fi

echo "Using uv at: $UV_PATH"

# Run the FastAPI server using uv
exec "$UV_PATH" run uvicorn cortex.app:app --host 0.0.0.0 --port 8000
