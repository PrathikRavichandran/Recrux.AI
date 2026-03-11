from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from models.schemas import ResumeParseOutput, JobSearchOutput, JobMatchScoreOutput

from agents.resume_agent import process_resume
from agents.job_search_agent import search_jobs
from agents.job_match_agent import score_jobs
from utils.file_parser import extract_text_from_file

router = APIRouter()

@router.post("/resume/parse", response_model=ResumeParseOutput, tags=["Agents"])
async def parse_resume(file: UploadFile = File(...)):
    """
    Endpoint to process a resume file (PDF/docx), extract skills and calculate an ATS score limit.
    """
    try:
        # Extract text using file parser utility
        text = await extract_text_from_file(file)
        
        # Pass to Resume Agent
        result = await process_resume(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/jobs/search", response_model=JobSearchOutput, tags=["Agents"])
async def find_jobs(skills: str = Form(...), role_name: str = Form(...)):
    """
    Endpoint taking skills list (comma separated string) and role_name to fetch matching jobs using the Job Search Agent.
    """
    try:
        # Convert comma separated string to list
        skills_list = [s.strip() for s in skills.split(",") if s.strip()]
        
        # Pass to Job Search Agent
        jobs = await search_jobs(skills_list, role_name)
        return JobSearchOutput(jobs=jobs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/jobs/score", response_model=JobMatchScoreOutput, tags=["Agents"])
async def calculate_scores(
    resume_text: str = Form(...),
    job_descriptions: List[str] = Form(...),
    job_ids: List[str] = Form(...)
):
    """
    Endpoint to score job descriptions against a given resume.
    """
    if len(job_descriptions) != len(job_ids):
        raise HTTPException(status_code=400, detail="Length of job_descriptions and job_ids must be equal.")
        
    try:
        scores = await score_jobs(resume_text, job_descriptions, job_ids)
        return JobMatchScoreOutput(scores=scores)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
