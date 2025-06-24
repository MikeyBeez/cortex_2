#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  ReadResourceRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

import { handleLoadModule, handleUnloadModule, handleListModules } from './handlers/modules.js';
import { handlePushContext, handleAnalyzeContext } from './handlers/context.js';
import { handleLoadIdentity, handleApplyPersona } from './handlers/identity.js';
import { handleGetMemoryUsage, handleOptimizeMemory } from './handlers/resources.js';
import { handleProvideFeedback } from './handlers/learning.js';
import { TOOLS } from './tools.js';
import { RESOURCES } from './resources.js';
import { CortexBridge } from './bridge.js';

// Initialize Cortex bridge
const cortex = new CortexBridge();

// Create MCP server
const server = new Server(
  {
    name: 'cortex-mcp',
    version: '0.1.0',
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  }
);

// Handle tool listing
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: TOOLS,
}));

// Handle resource listing
server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: RESOURCES,
}));

// Handle resource reading
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const { uri } = request.params;

  switch (uri) {
    case 'cortex://modules/catalog':
      return {
        contents: [
          {
            uri,
            mimeType: 'application/json',
            text: JSON.stringify(await cortex.getModuleCatalog(), null, 2),
          },
        ],
      };

    case 'cortex://state/current':
      return {
        contents: [
          {
            uri,
            mimeType: 'application/json',
            text: JSON.stringify(await cortex.getCurrentState(), null, 2),
          },
        ],
      };

    case 'cortex://metrics/learning':
      return {
        contents: [
          {
            uri,
            mimeType: 'application/json',
            text: JSON.stringify(await cortex.getLearningMetrics(), null, 2),
          },
        ],
      };

    default:
      throw new Error(`Unknown resource: ${uri}`);
  }
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      // Module management
      case 'load_module':
        return await handleLoadModule(cortex, args);
      case 'unload_module':
        return await handleUnloadModule(cortex, args);
      case 'list_modules':
        return await handleListModules(cortex, args);

      // Context management
      case 'push_context':
        return await handlePushContext(cortex, args);
      case 'analyze_context':
        return await handleAnalyzeContext(cortex, args);

      // Identity management
      case 'load_identity':
        return await handleLoadIdentity(cortex, args);
      case 'apply_persona':
        return await handleApplyPersona(cortex, args);

      // Resource management
      case 'get_memory_usage':
        return await handleGetMemoryUsage(cortex, args);
      case 'optimize_memory':
        return await handleOptimizeMemory(cortex, args);

      // Learning system
      case 'provide_feedback':
        return await handleProvideFeedback(cortex, args);

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${error instanceof Error ? error.message : String(error)}`,
        },
      ],
    };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  
  // Initialize Cortex connection
  await cortex.initialize();
  
  console.error('Cortex MCP server started');
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
