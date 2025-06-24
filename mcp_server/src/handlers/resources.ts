import { CortexBridge } from '../bridge.js';
import { getMemoryUsageSchema, optimizeMemorySchema } from '../tools.js';

export async function handleGetMemoryUsage(cortex: CortexBridge, args: any) {
  getMemoryUsageSchema.parse(args); // Validate (empty schema)
  
  const usage = await cortex.getMemoryUsage();
  
  const moduleList = usage.modules
    .map(m => `  - ${m.id}: ${m.size.toLocaleString()} tokens`)
    .join('\n');
  
  return {
    content: [
      {
        type: 'text',
        text: `Memory Usage:
- Used: ${usage.used.toLocaleString()} / ${usage.limit.toLocaleString()} tokens
- Free: ${(usage.limit - usage.used).toLocaleString()} tokens
- Usage: ${((usage.used / usage.limit) * 100).toFixed(1)}%

Loaded Modules:
${moduleList}`,
      },
    ],
  };
}

export async function handleOptimizeMemory(cortex: CortexBridge, args: any) {
  const { target_free } = optimizeMemorySchema.parse(args);
  
  const freed = await cortex.optimizeMemory(target_free);
  
  return {
    content: [
      {
        type: 'text',
        text: `Memory optimization complete:
- Freed: ${freed.toLocaleString()} tokens
- Modules moved to lower storage tiers`,
      },
    ],
  };
}
