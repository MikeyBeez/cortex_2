import { CortexBridge } from '../bridge.js';
import { provideFeedbackSchema } from '../tools.js';

export async function handleProvideFeedback(cortex: CortexBridge, args: any) {
  const { interaction_id, success, modules_helpful } = provideFeedbackSchema.parse(args);
  
  await cortex.provideFeedback(interaction_id, success, modules_helpful);
  
  const feedbackType = success ? 'positive' : 'negative';
  const helpfulText = modules_helpful 
    ? `\nHelpful modules: ${modules_helpful.join(', ')}`
    : '';
  
  return {
    content: [
      {
        type: 'text',
        text: `Feedback recorded:
- Interaction: ${interaction_id}
- Type: ${feedbackType}${helpfulText}

The learning system will use this to improve future module selection.`,
      },
    ],
  };
}
