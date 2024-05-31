from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model_name="gpt-4o")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
output_parser = StrOutputParser()

chain = prompt | llm | output_parser
results = chain.invoke({"input": "why is the sky blue?"})

print(results)