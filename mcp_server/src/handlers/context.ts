import { CortexBridge } from '../bridge.js';
import { pushContextSchema, analyzeContextSchema } from '../tools.js';

export async function handlePushContext(cortex: CortexBridge, args: any) {
  const context = pushContextSchema.parse(args);
  
  await cortex.pushContext(context);
  
  const parts = [];
  if (context.domain) parts.push(`domain: ${context.domain}`);
  if (context.keywords) parts.push(`keywords: ${context.keywords.join(', ')}`);
  if (context.intent) parts.push(`intent: ${context.intent}`);
  
  return {
    content: [
      {
        type: 'text',
        text: `Context updated: ${parts.join(', ')}`,
      },
    ],
  };
}

export async function handleAnalyzeContext(cortex: CortexBridge, args: any) {
  const { input } = analyzeContextSchema.parse(args);
  
  const analysis = await cortex.analyzeContext(input);
  
  return {
    content: [
      {
        type: 'text',
        text: `Context Analysis:
- Keywords: ${analysis.keywords.join(', ')}
- Domain: ${analysis.domain}
- Intent: ${analysis.intent}
- Confidence: ${(analysis.confidence * 100).toFixed(1)}%
- Suggested modules: ${analysis.suggested_modules.join(', ')}`,
      },
    ],
  };
}
