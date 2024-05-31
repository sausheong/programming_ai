from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

client = MistralClient()

chat_response = client.chat(
    model="mistral-large-latest",
    messages=[
        ChatMessage(role="user", content="Why is the sky blue?")
    ],
)

print(chat_response.choices[0].message.content)