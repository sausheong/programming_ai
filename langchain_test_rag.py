import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pydantic._migration')
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

def extract(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

model = ChatOpenAI(model="gpt-4o")
vectorstore = DocArrayInMemorySearch.from_texts(
    texts=extract('data/hansard.txt'),
    embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()
setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)
chain = setup_and_retrieval | prompt | model | output_parser

results = chain.invoke("How has Smart Nation improved citizen's lives?")
print(results)