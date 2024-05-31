from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

Settings.llm = OpenAI(model="gpt-4o")
messages = [
    ChatMessage(
        role="system", content="You are a helpful assistant."
    ),
    ChatMessage(role="user", content="Why is the sky blue?"),
]
resp = OpenAI().chat(messages)
print(resp)