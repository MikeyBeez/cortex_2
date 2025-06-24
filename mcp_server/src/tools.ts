import { z } from 'zod';

// Module management tools
export const loadModuleSchema = z.object({
  module_id: z.string(),
  priority: z.enum(['low', 'normal', 'high']).optional(),
});

export const unloadModuleSchema = z.object({
  module_id: z.string(),
  force: z.boolean().optional(),
});

export const listModulesSchema = z.object({
  filter: z.enum(['all', 'loaded', 'available']).optional(),
  type: z.enum(['knowledge', 'capability', 'identity', 'memory']).optional(),
});

// Context management tools
export const pushContextSchema = z.object({
  domain: z.string().optional(),
  keywords: z.array(z.string()).optional(),
  intent: z.string().optional(),
});

export const analyzeContextSchema = z.object({
  input: z.string(),
});

// Identity management tools
export const loadIdentitySchema = z.object({
  identity_id: z.string(),
});

export const applyPersonaSchema = z.object({
  persona_id: z.string(),
});

// Resource management tools
export const getMemoryUsageSchema = z.object({});

export const optimizeMemorySchema = z.object({
  target_free: z.number().optional(),
});

// Learning system tools
export const provideFeedbackSchema = z.object({
  interaction_id: z.string(),
  success: z.boolean(),
  modules_helpful: z.array(z.string()).optional(),
});

// Tool definitions
export const TOOLS = [
  {
    name: 'load_module',
    description: 'Load a cognitive module into active memory',
    inputSchema: {
      type: 'object',
      properties: {
        module_id: { type: 'string', description: 'ID of the module to load' },
        priority: { 
          type: 'string', 
          enum: ['low', 'normal', 'high'],
          description: 'Loading priority'
        },
      },
      required: ['module_id'],
    },
  },
  {
    name: 'unload_module',
    description: 'Unload a module from active memory',
    inputSchema: {
      type: 'object',
      properties: {
        module_id: { type: 'string', description: 'ID of the module to unload' },
        force: { type: 'boolean', description: 'Force unload even with dependencies' },
      },
      required: ['module_id'],
    },
  },
  {
    name: 'list_modules',
    description: 'List cognitive modules',
    inputSchema: {
      type: 'object',
      properties: {
        filter: { 
          type: 'string',
          enum: ['all', 'loaded', 'available'],
          description: 'Filter modules by status'
        },
        type: {
          type: 'string',
          enum: ['knowledge', 'capability', 'identity', 'memory'],
          description: 'Filter modules by type'
        },
      },
    },
  },
  {
    name: 'push_context',
    description: 'Push context information to influence module loading',
    inputSchema: {
      type: 'object',
      properties: {
        domain: { type: 'string', description: 'Domain of discourse' },
        keywords: { 
          type: 'array',
          items: { type: 'string' },
          description: 'Keywords in the context'
        },
        intent: { type: 'string', description: 'User intent' },
      },
    },
  },
  {
    name: 'analyze_context',
    description: 'Analyze input text to determine context and suggest modules',
    inputSchema: {
      type: 'object',
      properties: {
        input: { type: 'string', description: 'Input text to analyze' },
      },
      required: ['input'],
    },
  },
  {
    name: 'load_identity',
    description: 'Load an identity configuration',
    inputSchema: {
      type: 'object',
      properties: {
        identity_id: { type: 'string', description: 'ID of the identity to load' },
      },
      required: ['identity_id'],
    },
  },
  {
    name: 'apply_persona',
    description: 'Apply a persona overlay to current identity',
    inputSchema: {
      type: 'object',
      properties: {
        persona_id: { type: 'string', description: 'ID of the persona to apply' },
      },
      required: ['persona_id'],
    },
  },
  {
    name: 'get_memory_usage',
    description: 'Get current memory usage statistics',
    inputSchema: {
      type: 'object',
      properties: {},
    },
  },
  {
    name: 'optimize_memory',
    description: 'Optimize memory usage by moving modules between storage tiers',
    inputSchema: {
      type: 'object',
      properties: {
        target_free: { 
          type: 'number',
          description: 'Target amount of free memory in tokens'
        },
      },
    },
  },
  {
    name: 'provide_feedback',
    description: 'Provide feedback on module effectiveness',
    inputSchema: {
      type: 'object',
      properties: {
        interaction_id: { type: 'string', description: 'ID of the interaction' },
        success: { type: 'boolean', description: 'Was the interaction successful?' },
        modules_helpful: {
          type: 'array',
          items: { type: 'string' },
          description: 'Which modules were helpful?'
        },
      },
      required: ['interaction_id', 'success'],
    },
  },
];
