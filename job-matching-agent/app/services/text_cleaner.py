import re
from html import unescape


def clean_html(text: str) -> str:

    if not text:
        return ""

    # Convert HTML entities such as &nbsp;
    text = unescape(text)

    # Remove HTML tags such as <b>, </b>
    text = re.sub(r"<[^>]+>", " ", text)

    # Replace multiple spaces/newlines
    text = re.sub(r"\s+", " ", text)

    return text.strip()
