import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic();

const completion = await anthropic.messages.create({
  model: "claude-3-haiku-20240307",
  max_tokens: 1024,
  messages: [
    {"role": "user", "content": "Why is the sky blue?"}
  ]
});

console.log(completion);