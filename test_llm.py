from src.llm import LLMGenerator


llm = LLMGenerator()

answer = llm.generate(
    """
Question:
Why can a bank freeze a customer account?

Answer:
"""
)

print(answer)