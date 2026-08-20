from pydantic import BaseModel
from datetime import date

class ActasCreate(BaseModel):
    title: str
    meeting_date: date
    attendees: str
    topics: str
    agreements: str
    content: str
    community_id: int


class ActasUpdate(BaseModel):
    title: str
    meeting_date: date
    attendees: str
    topics: str
    agreements: str
    content: str
    community_id: int


class GenerateActaRequest(BaseModel):
    title: str
    attendees: str
    topics: str
    agreements: str