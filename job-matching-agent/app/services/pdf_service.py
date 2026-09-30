import pymupdf


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from all pages of a PDF.
    """

    document = pymupdf.open(pdf_path)

    text = ""

    for page_number, page in enumerate(document, start=1):
        page_text = page.get_text()

        text += f"\n--- Page {page_number} ---\n"
        text += page_text

    document.close()

    return text
