from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.generators import OpenAIGenerator
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.converters import TextFileToDocument
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.writers import DocumentWriter


document_store = InMemoryDocumentStore()
prompt_template = """
Given this documents, answer the question.
Documents:
{% for doc in documents %}
    {{ doc.content }}
{% endfor %}
Question: {{question}}
Answer:
"""

data_pipeline = Pipeline()
data_pipeline.add_component("converter", TextFileToDocument())
data_pipeline.add_component("cleaner", DocumentCleaner())
data_pipeline.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=5))
data_pipeline.add_component("writer", DocumentWriter(document_store=document_store))

data_pipeline.connect("converter", "cleaner")
data_pipeline.connect("cleaner", "splitter")
data_pipeline.connect("splitter", "writer")

data_pipeline.run({"converter": {"sources": ["data/hansard.txt"]}})

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", InMemoryBM25Retriever(document_store=document_store))
rag_pipeline.add_component("prompt_builder", PromptBuilder(template=prompt_template))
rag_pipeline.add_component("llm", OpenAIGenerator())

rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "How has Smart Nation improved citizen's lives?"
results = rag_pipeline.run({
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    }
)

print(results["llm"]["replies"][0])