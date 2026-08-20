from fastapi import APIRouter

from app.schemas.ai import (
    IncidentAnalysisRequest,
    IncidentAnalysisResponse,
    MinuteGenerationRequest,
    MinuteGenerationResponse,
)

from app.services.ai_service import (
    analyze_incident,
    generate_minute
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post(
    "/analyze-incident",
    response_model=IncidentAnalysisResponse
)
def analyze_incident_endpoint(
    data: IncidentAnalysisRequest
):

    return analyze_incident(data.description)


@router.post(
    "/generate-minute",
    response_model=MinuteGenerationResponse
)
def generate_minute_endpoint(
    data: MinuteGenerationRequest
):

    content = generate_minute(data)

    return {
        "content": content
    }