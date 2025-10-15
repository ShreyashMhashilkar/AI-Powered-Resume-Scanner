import io
from PyPDF2 import PdfReader
from docx import Document
import spacy
from sentence_transformers import SentenceTransformer, util
import re

# Load models once
nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# ------------------- Text Extraction -------------------
def extract_text(content: bytes, filename: str) -> str:
    """Extract text from PDF, DOCX, or TXT files."""
    if filename.lower().endswith(".pdf"):
        try:
            reader = PdfReader(io.BytesIO(content))
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except:
            return ""
    elif filename.lower().endswith(".docx"):
        try:
            doc = Document(io.BytesIO(content))
            text = "\n".join([p.text for p in doc.paragraphs])
            return text
        except:
            return ""
    else:
        try:
            return content.decode("utf-8")
        except:
            return ""

# ------------------- Skill Extraction -------------------
def extract_skills(text: str):
    """Extract skills dynamically using NLP."""
    doc = nlp(text)
    skills = set()

    # Extract named entities (ORG, PRODUCT, WORK_OF_ART) as potential skills
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART"]:
            skills.add(ent.text)

    # Extract proper nouns and nouns
    for token in doc:
        if token.pos_ in ["PROPN", "NOUN"] and len(token.text) > 2:
            skills.add(token.text)

    return list(skills)[:20]  # limit top 20 skills

# ------------------- Structured Resume Parsing -------------------
def parse_resume_sections(text: str):
    """Return structured resume sections for consistent display."""
    sections = {
        "name": "",
        "contact": "",
        "skills": extract_skills(text),
        "education": "",
        "experience": "",
        "projects": ""
    }

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    sections["contact"] = email_match.group(0) if email_match else ""

    # Extract phone number
    phone_match = re.search(r'(\+?\d{1,3})?[\s-]?\(?\d{2,4}\)?[\s-]?\d{5,10}', text)
    if phone_match:
        sections["contact"] += " | " + phone_match.group(0) if sections["contact"] else phone_match.group(0)

    # Extract Education
    edu_pattern = r'(Education|EDUCATION|Academic Qualifications)(:)?\s*(.*?)(Experience|Projects|$)'
    edu_match = re.search(edu_pattern, text, re.IGNORECASE | re.DOTALL)
    if edu_match:
        sections["education"] = edu_match.group(3).strip().replace("\n", " ")

    # Extract Experience
    exp_pattern = r'(Experience|WORK EXPERIENCE|Professional Experience)(:)?\s*(.*?)(Education|Projects|$)'
    exp_match = re.search(exp_pattern, text, re.IGNORECASE | re.DOTALL)
    if exp_match:
        sections["experience"] = exp_match.group(3).strip().replace("\n", " ")

    # Extract Projects
    proj_pattern = r'(Projects|PROJECTS)(:)?\s*(.*?)(Education|Experience|$)'
    proj_match = re.search(proj_pattern, text, re.IGNORECASE | re.DOTALL)
    if proj_match:
        sections["projects"] = proj_match.group(3).strip().replace("\n", " ")

    # Extract Name (first non-empty line)
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    sections["name"] = lines[0] if lines else "N/A"

    return sections

# ------------------- Semantic Similarity -------------------
def compute_similarity(jd_text: str, resume_texts: list):
    """Compute semantic similarity between JD and resumes."""
    jd_embedding = embedding_model.encode(jd_text, convert_to_tensor=True)
    resume_embeddings = embedding_model.encode(resume_texts, convert_to_tensor=True)
    similarities = util.cos_sim(jd_embedding, resume_embeddings).cpu().numpy().flatten()
    return similarities

# ------------------- Rank and Structure Results -------------------
def rank_resumes(jd: str, resumes_contents: list, resumes_filenames: list):
    """
    jd: job description text
    resumes_contents: list of resume texts
    resumes_filenames: list of original filenames
    Returns: list of dicts with structured info + similarity score
    """
    similarities = compute_similarity(jd, resumes_contents)
    ranked_indices = similarities.argsort()[::-1]  # descending order

    results = []
    for rank, idx in enumerate(ranked_indices, start=1):
        parsed = parse_resume_sections(resumes_contents[idx])
        results.append({
            "rank": rank,
            "score": round(float(similarities[idx]), 4),
            "filename": resumes_filenames[idx],
            **parsed
        })
    return results
