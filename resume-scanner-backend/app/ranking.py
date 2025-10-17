from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .resume_processor import extract_skills

def compute_similarity(jd_text: str, resume_texts: list):
    """
    Compute cosine similarity using TF-IDF (lightweight alternative).
    """
    all_docs = [jd_text] + resume_texts
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(all_docs)

    jd_vec = tfidf_matrix[0:1]
    resume_vecs = tfidf_matrix[1:]
    similarities = cosine_similarity(jd_vec, resume_vecs).flatten()
    return similarities


def rank_resumes(jd: str, resume_texts: list, filenames: list):
    """
    Rank resumes by TF-IDF similarity score and extract skills.
    """
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