# Recrux.AI — Intelligent Multi-Agent Job Matching

> **Status:** Backend agents fully implemented. Frontend currently ships as a static UI showcase — backend wiring is the next milestone (see roadmap below).

A job-discovery and matching platform powered by a multi-agent AI architecture. Google Gemini + LangGraph orchestrate three specialized agents (resume parser, job searcher, match scorer) behind a FastAPI service. A separate React/Vite frontend shows the intended product UX.

## Architecture

```
                    ┌─────────────────────────┐
                    │   React + Vite SPA      │
                    │   (frontend/)           │
                    │   static UI showcase    │
                    └───────────┬─────────────┘
                                │
                                │  (planned — currently mock data)
                                ▼
┌──────────────────────────────────────────────────────┐
│            FastAPI backend  (backend/)               │
│            CORS-restricted, env-driven origins       │
│                                                      │
│  /api/agents  →  LangGraph workflow                  │
│       │                                              │
│       ├──▶ resume_agent     (PyMuPDF / python-docx)  │
│       ├──▶ job_search_agent (mock JSON corpus)       │
│       └──▶ job_match_agent  (Gemini scoring)         │
└──────────────────────────────────────────────────────┘
```

## Tech stack

| Layer | Tech |
|---|---|
| Frontend | React 19, Vite 6, TypeScript 5.8, Tailwind 4, Lucide, Motion |
| Backend | FastAPI, LangGraph, LangChain, `langchain-google-genai` |
| LLM | Google Gemini |
| File parsing | PyMuPDF (PDF), `python-docx` (DOCX) |
| Data | Pydantic v2; mock job corpus in `backend/utils/dummy_jobs.json` |

## Run locally

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # then add your GEMINI_API_KEY
uvicorn main:app --reload            # http://localhost:8000
```

Open <http://localhost:8000/docs> for the interactive Swagger UI — the easiest way to demo the agents end-to-end without the frontend.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local           # then set VITE_API_URL
npm run dev                          # http://localhost:3000
```

## Deploy

Get a Gemini API key first: <https://aistudio.google.com/app/apikey>.

### Backend → Hugging Face Spaces (Docker, free)

1. Create a new Space at <https://huggingface.co/new-space> with `SDK = Docker`.
2. Push the `backend/` directory to the Space (or link via the Spaces UI; HF auto-detects the `backend/Dockerfile`).
3. In **Settings → Variables and secrets**, add:
   - `GEMINI_API_KEY` (secret)
   - `ALLOWED_ORIGINS` = your Vercel frontend URL once it's deployed (e.g. `https://recrux-ai.vercel.app`)
4. The Space exposes port `7860`; Swagger UI is available at `/docs`.

### Frontend → Vercel (free)

1. Create a project at <https://vercel.com/new>, import this repo.
2. **Root directory**: `frontend`
3. Vercel auto-detects Vite. Build command: `npm run build`, Output: `dist`.
4. **Environment variables**: `VITE_API_URL` = your HF Space URL.
5. After first deploy, copy the Vercel URL back into the HF Space's `ALLOWED_ORIGINS` so CORS lets the frontend in.

## Roadmap

- [ ] **Wire frontend → backend.** Add resume upload, dispatch to `/api/agents`, render scored matches.
- [ ] **Live job APIs.** Replace `dummy_jobs.json` with LinkedIn or JSearch.
- [ ] **Vector store.** ChromaDB integration is in `requirements.txt` but not yet wired into the agent graph.
- [ ] **Auth.** Google OAuth + email/password.

## License

Reserved for Recrux.AI Team.
