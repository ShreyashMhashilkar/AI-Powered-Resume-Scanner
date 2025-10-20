from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.resume_processor import extract_text
from app.ranking import rank_resumes

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scan")
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

@app.get("/")
async def root():
    return {"message": "AI Resume Scanner Backend is Running (Vercel Serverless)"}
