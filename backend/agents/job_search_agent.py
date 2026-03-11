import json
import os
from typing import List
from models.schemas import JobListing

async def search_jobs(skills: List[str], role_name: str) -> List[JobListing]:
    """
    Simulates finding top 10-20 most recent matching jobs from open-source APIs.
    Currently uses dummy_jobs.json to imitate job search api response.
    """
    # Path to the dummy file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dummy_file_path = os.path.join(current_dir, "..", "utils", "dummy_jobs.json")
    
    try:
        with open(dummy_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            # Simple simulation: return all as JobListing models
            jobs = [JobListing(**job) for job in data]
            return jobs
            
    except FileNotFoundError:
        print("Dummy jobs file not found.")
        return []
    except Exception as e:
        print(f"Error reading dummy jobs: {e}")
        return []
