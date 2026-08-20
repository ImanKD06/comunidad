from pydantic import BaseModel
from datetime import date

class IncidentCreate(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    created_at: date
    community_id: int


class IncidentUpdate(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    created_at: date
    community_id: int



class IncidentClassificationRequest(BaseModel):
    description: str

