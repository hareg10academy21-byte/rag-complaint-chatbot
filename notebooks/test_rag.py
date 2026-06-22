from src.retriever import Retriever
from src.rag_pipeline import RAGPipeline

retriever = Retriever(
    "vector_store/complaints_index.faiss",
    "vector_store/metadata.csv"
)

rag = RAGPipeline(retriever)

question = "Why are customers unhappy with credit cards?"

result = rag.run(question)

print("\nANSWER:\n", result["answer"])

print("\nTOP SOURCES:\n")
for c in result["contexts"]:
    print("-", c["chunk_text"][:200])