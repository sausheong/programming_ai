from openai import OpenAI
client = OpenAI(
    base_url="http://34.142.153.101/v1",
    api_key="abc123",    
)

completion = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3-8B-Instruct",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Why is the sky blue?"}
  ]
)

print(completion.choices[0].message.content)
