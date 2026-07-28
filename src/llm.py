# from transformers import pipeline
# import time

# class LLMGenerator:
#     def __init__(self):
#         self.pipe = pipeline(
#             "text-generation",
#             model="google/flan-t5-base",
#             max_new_tokens=256
#         )

#     def generate(self, prompt):
#         result = self.pipe(
#             prompt,
#             max_new_tokens=256,
#             do_sample=False
#         )[0]["generated_text"]

#         # remove prompt echo if model repeats it
#         if "Answer" in result:
#             result = result.split("Answer")[-1]

#         return result.strip()

#     # ----------------------------
#     # STREAMING SIMULATION (ChatGPT-like effect)
#     # ----------------------------
#     def stream_generate(self, prompt, delay=0.03):
#         result = self.pipe(
#             prompt,
#             max_new_tokens=256,
#             do_sample=False
#         )[0]["generated_text"]

#         output = ""

#         for char in result:
#             output += char
#             time.sleep(delay)
#             yield output

import time
from transformers import pipeline

from src.config import ModelConfig


config = ModelConfig()


class LLMGenerator:
    """
    Handles response generation using the configured language model.
    """

    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model=config.llm_model,
            max_new_tokens=config.max_new_tokens,
        )

    def generate(self, prompt: str) -> str:
        """
        Generate a complete response.
        """

        result = self.pipe(
            prompt,
            max_new_tokens=config.max_new_tokens,
            do_sample=False,
        )[0]["generated_text"]

        if "Answer" in result:
            result = result.split("Answer")[-1]

        return result.strip()

    def stream_generate(
        self,
        prompt: str,
        delay: float = config.stream_delay,
    ):
        """
        Stream the generated response one character at a time.
        """

        result = self.pipe(
            prompt,
            max_new_tokens=config.max_new_tokens,
            do_sample=False,
        )[0]["generated_text"]

        output = ""

        for char in result:
            output += char
            time.sleep(delay)
            yield output