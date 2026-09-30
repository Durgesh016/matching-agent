from pydantic import BaseModel
from typing import List, Optional


class Job(BaseModel):
    category: str
    role: str
    skills: List[str]


class JobPosting(BaseModel):
    title: str
    company: str
    location: str
    experience: Optional[str] = None
    posted_date: Optional[str] = None
    posted_datetime: Optional[str] = None
    description: Optional[str] = None
    skills: List[str] = []
    source_url: Optional[str] = None


class JobSearchRequest(BaseModel):
    role: Optional[str] = None
    experience: Optional[str] = None
    location: Optional[str] = None
    posted_within: Optional[str] = None
