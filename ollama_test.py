from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser
results = chain.invoke({"input": "why is the sky blue?"})

print(results)