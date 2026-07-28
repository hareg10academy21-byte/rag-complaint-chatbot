from src.utils import join_contexts


def test_join_contexts():
    contexts = [
        {"chunk_text": "First"},
        {"chunk_text": "Second"},
    ]

    result = join_contexts(contexts)

    assert "First" in result
    assert "Second" in result