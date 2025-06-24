import { CortexBridge } from '../bridge.js';
import { loadModuleSchema, unloadModuleSchema, listModulesSchema } from '../tools.js';

export async function handleLoadModule(cortex: CortexBridge, args: any) {
  const { module_id, priority } = loadModuleSchema.parse(args);
  
  await cortex.loadModule(module_id, priority);
  
  return {
    content: [
      {
        type: 'text',
        text: `Successfully loaded module: ${module_id}`,
      },
    ],
  };
}

export async function handleUnloadModule(cortex: CortexBridge, args: any) {
  const { module_id, force } = unloadModuleSchema.parse(args);
  
  await cortex.unloadModule(module_id, force);
  
  return {
    content: [
      {
        type: 'text',
        text: `Successfully unloaded module: ${module_id}`,
      },
    ],
  };
}

export async function handleListModules(cortex: CortexBridge, args: any) {
  const { filter, type } = listModulesSchema.parse(args);
  
  const modules = await cortex.listModules(filter, type);
  
  const moduleList = modules.map(m => 
    `- ${m.id} (${m.type}): ${m.description} [${m.status}]`
  ).join('\n');
  
  return {
    content: [
      {
        type: 'text',
        text: `Found ${modules.length} modules:\n${moduleList}`,
      },
    ],
  };
}
