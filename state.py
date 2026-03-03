from typing import TypedDict, List

class CVState(TypedDict):
    cv_text: str
    job_text: str
    extracted_skills: List[str]
    score: float
    decision: str
    feedback: str
