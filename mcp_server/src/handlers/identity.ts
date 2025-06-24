import { CortexBridge } from '../bridge.js';
import { loadIdentitySchema, applyPersonaSchema } from '../tools.js';

export async function handleLoadIdentity(cortex: CortexBridge, args: any) {
  const { identity_id } = loadIdentitySchema.parse(args);
  
  await cortex.loadIdentity(identity_id);
  
  return {
    content: [
      {
        type: 'text',
        text: `Successfully loaded identity: ${identity_id}`,
      },
    ],
  };
}

export async function handleApplyPersona(cortex: CortexBridge, args: any) {
  const { persona_id } = applyPersonaSchema.parse(args);
  
  await cortex.applyPersona(persona_id);
  
  return {
    content: [
      {
        type: 'text',
        text: `Successfully applied persona: ${persona_id}`,
      },
    ],
  };
}
