from .resume_processor import extract_skills, compute_similarity

def rank_resumes(jd: str, resume_texts: list, filenames: list):
    similarities = compute_similarity(jd, resume_texts)
    ranked_indices = similarities.argsort()[::-1]

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