import re

def clean_text(text):

    text = str(text).lower()

    text = re.sub(
        r"i am writing to file a complaint",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()