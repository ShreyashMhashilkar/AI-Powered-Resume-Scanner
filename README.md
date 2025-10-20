
AI-powered resume ranking system built with Python, FastAPI, React.js, and NLP using Sentence Transformers. It extracts and parses resumes (PDF, DOCX, TXT), matches them to job descriptions semantically, and ranks candidates. Features a Material UI frontend, real-time feedback, and ranked candidate visualization.

__Features__

Extract text from resumes: PDF, DOCX, TXT
Semantic matching of resumes to job descriptions using Sentence Transformers
Rank candidates by relevance
Skill extraction from resumes
Material UI frontend for uploading resumes
Real-time feedback during file upload and ranking
Dynamic visualization of ranked candidates

**Tech Stack**
Backend: Python, FastAPI, Sentence Transformers, PyTorch, Transformers
Frontend: React.js, Material UI
NLP: Semantic similarity, BERT-based NER for skill extraction
File Parsing: PyPDF2, python-docx

**Installation**
1. Clone the repository
git clone <your-repo-url>
cd AI-Powered-Resume-Scanner

2. Backend Setup
cd backend  # or wherever your FastAPI code is
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


The backend should now be running at http://localhost:8000.

3. Frontend Setup
cd frontend  # or wherever your React code is
npm install
npm start


The frontend should open at http://localhost:3000.

**Usage**

Open the frontend in your browser.
Paste the Job Description.
Upload resumes (PDF, DOCX, TXT).
Click "Match & Rank Resumes".
View ranked candidates, matched skills, and snippets.

**API Endpoints**

GET / → Health check
POST /scan → Submit job description and resumes, returns ranked candidates

**Request example for /scan:**

POST /scan
Form Data:
- jd: string
- resumes: file[]


**Response example:**
```bash
{
  "results": [
    {
      "rank": 1,
      "score": 0.9234,
      "resume_filename": "John_Doe.pdf",
      "matched_skills": ["Python", "FastAPI", "React"],
      "num_skills_matched": 3,
      "resume_snippet": "Experienced software engineer..."
    }
  ]
}
