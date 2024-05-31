import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

print(message.content[0].text)