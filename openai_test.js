import OpenAI from "openai";

const openai = new OpenAI();

const completion = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Why is the sky blue?" }
  ],    
});

console.log(completion.choices[0]);