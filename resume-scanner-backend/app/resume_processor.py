import io
from PyPDF2 import PdfReader
from docx import Document
from .models import get_ner_pipeline, get_spacy_nlp

def extract_text(content: bytes, filename: str) -> str:
    """Extract text from PDF, DOCX, or TXT files."""
    if filename.lower().endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(content))
            return "".join([page.extract_text() + "\n" for page in reader.pages if page.extract_text()])
        except:
            return ""
    elif filename.lower().endswith(".docx"):
        try:
            doc = Document(io.BytesIO(content))
            return "\n".join([p.text for p in doc.paragraphs])
        except:
            return ""
    else:
        try:
            return content.decode("utf-8")
        except:
            return ""

def extract_skills(text: str):
    """Extract top skills using transformer-based NER (fallback to spaCy)."""
    try:
        ner_pipeline = get_ner_pipeline()
        entities = ner_pipeline(text)
        skills = set()
        for ent in entities:
            if ent["entity_group"] in ["ORG", "MISC", "PER"]:  # Customize for skill-like entities
                skills.add(ent["word"])
        if skills:
            return list(skills)[:30]
    except:
        pass

    # Fallback spaCy
    nlp = get_spacy_nlp()
    doc = nlp(text)
    skills = set()
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART"]:
            skills.add(ent.text)
    for token in doc:
        if token.pos_ in ["PROPN", "NOUN"] and len(token.text) > 2:
            skills.add(token.text)
    return list(skills)[:30]
