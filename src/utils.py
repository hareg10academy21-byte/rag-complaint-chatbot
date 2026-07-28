from typing import List


def join_contexts(contexts: List[dict]) -> str:
    """
    Combine retrieved document chunks into a single context string.
    """
    return "\n\n".join(
        context["chunk_text"]
        for context in contexts
    )