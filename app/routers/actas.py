from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.actas import Actas
from app.schemas.actas import ActasCreate, ActasUpdate
from app.services.ai_service import redactar_acta


router = APIRouter(prefix="/actas", tags=["Actas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/generate")
def generate_acta(data: ActasCreate):
    content = redactar_acta(
        title=data.title,
        date=getattr(data, "meeting_date", getattr(data, "date", "")),
        attendees=data.attendees,
        topics=data.topics,
        agreements=data.agreements,
        community_name=getattr(data, "community_name", "")
    )

    return {
        "content": content,
        "contenido": content
    }


@router.get("")
def get_actas(db: Session = Depends(get_db)):
    return db.query(Actas).all()


@router.get("/{acta_id}")
def get_acta(acta_id: int, db: Session = Depends(get_db)):
    acta = db.query(Actas).filter(Actas.id == acta_id).first()

    if not acta:
        raise HTTPException(
            status_code=404,
            detail="Acta not found"
        )

    return acta


@router.post("")
def create_actas(data: ActasCreate, db: Session = Depends(get_db)):
    new_acta = Actas(
        title=data.title,
        meeting_date=data.meeting_date,
        attendees=data.attendees,
        topics=data.topics,
        agreements=data.agreements,
        content=data.content,
        community_id=data.community_id
    )

    db.add(new_acta)
    db.commit()
    db.refresh(new_acta)

    return new_acta


@router.put("/{acta_id}")
def update_acta(
    acta_id: int,
    data: ActasUpdate,
    db: Session = Depends(get_db)
):
    acta = db.query(Actas).filter(Actas.id == acta_id).first()

    if not acta:
        raise HTTPException(
            status_code=404,
            detail="Acta not found"
        )

    acta.title = data.title
    acta.meeting_date = data.meeting_date
    acta.attendees = data.attendees
    acta.topics = data.topics
    acta.agreements = data.agreements
    acta.content = data.content
    acta.community_id = data.community_id

    db.commit()
    db.refresh(acta)

    return acta


@router.delete("/{acta_id}")
def delete_acta(acta_id: int, db: Session = Depends(get_db)):
    acta = db.query(Actas).filter(Actas.id == acta_id).first()

    if not acta:
        raise HTTPException(status_code=404, detail="Acta not found")

    db.delete(acta)
    db.commit()

    return {"message": "Deleted"}