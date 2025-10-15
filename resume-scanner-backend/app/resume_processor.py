# app/resume_processor.py
import io
import re
from PyPDF2 import PdfReader
from docx import Document
from .models import get_nlp, get_embedding_model
from sentence_transformers import util

# ------------------- Text Extraction -------------------
def extract_text(content: bytes, filename: str) -> str:
    if filename.lower().endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(content))
            text = "".join([page.extract_text() + "\n" for page in reader.pages])
            return text
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

# ------------------- Skill Extraction -------------------
def extract_skills(text: str):
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

# ------------------- Semantic Similarity -------------------
def compute_similarity(jd_text: str, resume_texts: list):
    model = get_embedding_model()
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)
    similarities = util.cos_sim(jd_embedding, resume_embeddings).cpu().numpy().flatten()
    return similarities
