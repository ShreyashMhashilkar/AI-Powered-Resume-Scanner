from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def create_app():
    app = FastAPI(title="AI-Powered Resume Scanner (Advanced ML)")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace with frontend URL in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
