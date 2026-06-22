from transformers import pipeline
import time

class LLMGenerator:
    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model="google/flan-t5-base",
            max_new_tokens=256
        )

    def generate(self, prompt):
        result = self.pipe(
            prompt,
            max_new_tokens=256,
            do_sample=False
        )[0]["generated_text"]

        # remove prompt echo if model repeats it
        if "Answer" in result:
            result = result.split("Answer")[-1]

        return result.strip()

    # ----------------------------
    # STREAMING SIMULATION (ChatGPT-like effect)
    # ----------------------------
    def stream_generate(self, prompt, delay=0.03):
        result = self.pipe(
            prompt,
            max_new_tokens=256,
            do_sample=False
        )[0]["generated_text"]

        output = ""

        for char in result:
            output += char
            time.sleep(delay)
            yield output