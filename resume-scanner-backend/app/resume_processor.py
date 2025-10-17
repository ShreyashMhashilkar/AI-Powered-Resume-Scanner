import io
from PyPDF2 import PdfReader
from docx import Document
from .models import get_nlp

def extract_text(content: bytes, filename: str) -> str:
    """
    Extract text from PDF, DOCX, or TXT files.
    """
    if filename.lower().endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(content))
            return "".join([page.extract_text() + "\n" for page in reader.pages if page.extract_text()])
        except Exception:
            return ""
    elif filename.lower().endswith(".docx"):
        try:
            doc = Document(io.BytesIO(content))
            return "\n".join([p.text for p in doc.paragraphs])
        except Exception:
            return ""
    else:
        try:
            return content.decode("utf-8")
        except Exception:
            return ""


def extract_skills(text: str):
    """
    Extract skills and entities using spaCy NLP.
    """
    nlp = get_nlp()
    doc = nlp(text)
    skills = set()

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART"]:
            skills.add(ent.text)

    for token in doc:
        if token.pos_ in ["PROPN", "NOUN"] and len(token.text) > 2:
            skills.add(token.text)

    return list(skills)[:20]