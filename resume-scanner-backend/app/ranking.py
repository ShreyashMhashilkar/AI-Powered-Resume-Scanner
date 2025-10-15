from .resume_processor import extract_skills, compute_similarity

def rank_resumes(jd: str, resume_texts: list, filenames: list):
    """Rank resumes using semantic similarity embeddings"""
    similarities = compute_similarity(jd, resume_texts)

    ranked = sorted(
        [(i, score, resume_texts[i]) for i, score in enumerate(similarities)],
        key=lambda x: x[1],
        reverse=True
    )

    results = []
    for idx, score, resume in ranked:
        matched_skills = extract_skills(resume)

        # Create a clean resume snippet (first 400 chars)
        snippet_length = 500
        resume_snippet = resume[:snippet_length]
        if len(resume) > snippet_length:
            resume_snippet += "..."

        results.append({
            "rank": idx + 1,
            "score": round(float(score), 4),
            "resume_filename": filenames[idx],
            "matched_skills": matched_skills,
            "num_skills_matched": len(matched_skills),
            "resume_snippet": resume_snippet
        })

    return results
