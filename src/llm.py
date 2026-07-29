import time
from functools import lru_cache

from transformers import pipeline

from src.config import ModelConfig


config = ModelConfig()


@lru_cache(maxsize=1)
def load_model():
    """
    Load and cache the language model.

    The model is loaded only once to improve application performance.
    """

    return pipeline(
        "text-generation",
        model=config.llm_model,
    )


class LLMGenerator:
    """
    Handles response generation using the configured language model.
    """

    def __init__(self):

        # Load cached model instead of downloading/loading repeatedly
        self.pipe = load_model()


    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a complete response.
        """

        result = self.pipe(
            prompt,
            max_new_tokens=config.max_new_tokens,
            do_sample=False,
        )[0]["generated_text"]

        return result.strip()


    def stream_generate(
        self,
        prompt: str,
        delay: float = config.stream_delay,
    ):
        """
        Stream generated response character by character.
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