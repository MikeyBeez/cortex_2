#!/bin/bash
# /Users/bard/Code/cortex_2/mcp_server/cortex-mcp.sh

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the MCP server with node
exec node "$DIR/dist/index.js"
