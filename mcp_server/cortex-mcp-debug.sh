#!/bin/bash
# /Users/bard/Code/cortex_2/mcp_server/cortex-mcp-debug.sh

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create log directory if it doesn't exist
mkdir -p "$DIR/logs"

# Run the MCP server with node and log errors
exec node "$DIR/dist/index.js" 2>"$DIR/logs/mcp-error.log"
