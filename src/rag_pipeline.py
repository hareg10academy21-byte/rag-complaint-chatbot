# from src.llm import LLMGenerator
# from src.utils import join_contexts
# class RAGPipeline:
#     def __init__(self, retriever):
#         self.retriever = retriever
#         self.llm = LLMGenerator()

#     def build_prompt(self, question, contexts):
#         context_text = "\n\n".join(
#             [c["chunk_text"] for c in contexts]
#         )

#         return f"""
# You are a financial analyst assistant for CrediTrust.

# Use ONLY the context below.

# Context:
# {context_text}

# Question:
# {question}

# Answer clearly and concisely.
# """

#     def retrieve(self, question):
#         return self.retriever.search(question, k=5)

#     def run_stream(self, question):
#         contexts = self.retrieve(question)
#         prompt = self.build_prompt(question, contexts)

#         return contexts, self.llm.stream_generate(prompt)

from typing import List, Dict, Tuple

from src.llm import LLMGenerator
from src.utils import join_contexts


class RAGPipeline:
    """
    Retrieval-Augmented Generation (RAG) pipeline that retrieves
    relevant complaint documents and generates responses using an LLM.
    """

    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMGenerator()

    def build_prompt(
        self,
        question: str,
        contexts: List[Dict]
    ) -> str:
        """
        Build a prompt for the language model.

        Args:
            question: User's question.
            contexts: Retrieved complaint chunks.

        Returns:
            Prompt string.
        """

        # Use reusable utility function
        context_text = join_contexts(contexts)

        return f"""
You are a financial analyst assistant for CrediTrust.

Use ONLY the context below.

Context:
{context_text}

Question:
{question}

Answer clearly and concisely.
"""

    def retrieve(self, question: str) -> List[Dict]:
        """
        Retrieve the most relevant complaint chunks.
        """
        return self.retriever.search(question, k=5)

    def run_stream(
        self,
        question: str
    ) -> Tuple[List[Dict], object]:
        """
        Retrieve context and stream the generated response.
        """
        contexts = self.retrieve(question)
        prompt = self.build_prompt(question, contexts)

        return contexts, self.llm.stream_generate(prompt)