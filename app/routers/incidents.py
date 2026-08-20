from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["Incidents"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()

@router.get("/{incident_id}")
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident

@router.post("/")
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    new_incident = Incident(
        title=incident.title,
        description=incident.description,
        status=incident.status,
        priority=incident.priority,
        created_at=incident.created_at,
        community_id=incident.community_id
    )

    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)

    return new_incident


@router.put("/{incident_id}")
def update_incident(
    incident_id: int,
    data: IncidentUpdate,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    incident.title = data.title
    incident.description = data.description
    incident.status = data.status
    incident.priority = data.priority
    incident.created_at = data.created_at
    incident.community_id = data.community_id

    db.commit()
    db.refresh(incident)

    return incident

@router.delete("/{incident_id}")
def delete_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    db.delete(incident)
    db.commit()

    return {"message": "Deleted"}



