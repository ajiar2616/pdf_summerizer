import fitz  # PyMuPDF

def extract_pdf_text(file_path):
    """
    Reads PDF and returns a dict with each page's content as a section.
    """
    doc = fitz.open(file_path)
    sections = {}

    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():  # Skip blank pages
            sections[f"Page {i}"] = text.strip()

    doc.close()
    return sections
