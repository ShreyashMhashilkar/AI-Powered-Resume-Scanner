from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from app.core import create_app
from app.resume_processor import extract_text
from app.ranking import rank_resumes

app: FastAPI = create_app()

@app.post("/match_rank")
async def match_rank(
    jd: str = Form(...), 
    resumes: List[UploadFile] = File(...)
):
    resume_texts = []
    filenames = []

    for r in resumes:
        content = await r.read()
        text = extract_text(content, r.filename)
        resume_texts.append(text)
        filenames.append(r.filename)

    results = rank_resumes(jd, resume_texts, filenames)
    return {"results": results}