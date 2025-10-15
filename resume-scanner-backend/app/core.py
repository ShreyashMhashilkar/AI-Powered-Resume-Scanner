from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def create_app():
    app = FastAPI(title="AI-Powered Resume Scanner")

    # Allow React frontend origin
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Change if frontend URL changes
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
