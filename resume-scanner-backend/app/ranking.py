from .resume_processor import extract_skills
from .models import get_rank_model
import torch
from sentence_transformers import util

def rank_resumes(jd: str, resume_texts: list, filenames: list):
    """Rank resumes using transformer embeddings + extract skills."""
    model = get_rank_model()

    # Encode JD and resumes
    jd_embedding = model.encode(jd, convert_to_tensor=True)
    resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)

    # Compute cosine similarity
    similarities = util.pytorch_cos_sim(jd_embedding, resume_embeddings).squeeze(0)

    ranked_indices = torch.argsort(similarities, descending=True)

    results = []
    for rank, idx in enumerate(ranked_indices, start=1):
        matched_skills = extract_skills(resume_texts[idx])
        snippet_length = 500
        resume_snippet = resume_texts[idx][:snippet_length]
        if len(resume_texts[idx]) > snippet_length:
            resume_snippet += "..."
        results.append({
            "rank": rank,
            "score": round(float(similarities[idx]), 4),
            "resume_filename": filenames[idx],
            "matched_skills": matched_skills,
            "num_skills_matched": len(matched_skills),
            "resume_snippet": resume_snippet
        })
    return results
