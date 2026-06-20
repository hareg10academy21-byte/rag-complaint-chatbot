from src.preprocessing import clean_text

def test_clean_text():
    text = "Hello!!! WORLD 123"
    result = clean_text(text)

    assert isinstance(result, str)
    assert result == "hello world"