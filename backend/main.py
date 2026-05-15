import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables FIRST before importing local modules that instantiate LLMs
load_dotenv()

from routers.agent_router import router as agent_router

app = FastAPI(
    title="Recrux.AI Agents Backend",
    description="Backend AI multi-agent architecture for Recrux.AI to parse resumes, find roles, and score matches.",
    version="1.0.0",
)

# CORS — restrict to known origins. Override via the ALLOWED_ORIGINS env var
# (comma-separated). Default keeps both common Vite dev ports working locally.
_default_origins = "http://localhost:3000,http://localhost:5173"
_allowed_origins = [
    origin.strip()
    for origin in os.environ.get("ALLOWED_ORIGINS", _default_origins).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agent_router, prefix="/api")


@app.get("/", tags=["Health"])
async def root():
    return {
        "message": "Recrux.AI Backend is running smoothly.",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
