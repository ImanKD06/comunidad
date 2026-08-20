from pydantic import BaseModel


class IncidentAnalysisRequest(BaseModel):
    description: str


class IncidentAnalysisResponse(BaseModel):
    category: str
    priority: str
    recommendation: str


class MinuteGenerationRequest(BaseModel):
    title: str
    attendees: str
    topics: str
    agreements: str


class MinuteGenerationResponse(BaseModel):
    content: str