from src.llm import LLMGenerator

class RAGPipeline:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMGenerator()

    def build_prompt(self, question, contexts):
        context_text = "\n\n".join(
            [c["chunk_text"] for c in contexts]
        )

        return f"""
You are a financial analyst assistant for CrediTrust.

Use ONLY the context below.

Context:
{context_text}

Question:
{question}

Answer clearly and concisely.
"""

    def retrieve(self, question):
        return self.retriever.search(question, k=5)

    def run_stream(self, question):
        contexts = self.retrieve(question)
        prompt = self.build_prompt(question, contexts)

        return contexts, self.llm.stream_generate(prompt)