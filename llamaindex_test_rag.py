from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

Settings.llm = OpenAI(model="gpt-4o")

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("How has Smart Nation improved citizen's lives?")
print(response)