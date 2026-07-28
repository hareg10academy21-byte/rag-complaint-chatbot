# from src.preprocessing import clean_text

# def test_clean_text():
#     text = "Hello!!! WORLD 123"
#     result = clean_text(text)

#     assert isinstance(result, str)
#     assert result == "hello world"

from src.preprocessing import clean_text


def test_clean_text_lowercase():
    assert clean_text("HELLO WORLD") == "hello world"


def test_clean_text_remove_special_characters():
    assert clean_text("Hello!!!") == "hello"


def test_clean_text_remove_boilerplate():
    text = "I am writing to file a complaint about my bank."

    cleaned = clean_text(text)

    assert "i am writing to file a complaint" not in cleaned


def test_clean_text_remove_extra_spaces():
    assert clean_text("Hello     World") == "hello world"


def test_clean_text_empty_string():
    assert clean_text("") == ""