from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def create_app():
    app = FastAPI(title="AI-Powered Resume Scanner")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace with your frontend URL in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app