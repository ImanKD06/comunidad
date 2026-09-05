from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.neighbor import Neighbor
from app.schemas.neighbor import NeighborCreate, NeighborUpdate


router = APIRouter(
    prefix="/neighbors",
    tags=["Neighbors"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_neighbors(db: Session = Depends(get_db)):
    return db.query(Neighbor).all()


@router.post("")
def create_neighbor(
    neighbor: NeighborCreate,
    db: Session = Depends(get_db)
):
    new_neighbor = Neighbor(
        name=neighbor.name,
        apartment=neighbor.apartment,
        phone=neighbor.phone,
        community_id=neighbor.community_id
    )

    db.add(new_neighbor)
    db.commit()
    db.refresh(new_neighbor)

    return new_neighbor


@router.delete("/{neighbor_id}")
def delete_neighbor(
    neighbor_id: int,
    db: Session = Depends(get_db)
):
    neighbor = (
        db.query(Neighbor)
        .filter(Neighbor.id == neighbor_id)
        .first()
    )

    if not neighbor:
        raise HTTPException(
            status_code=404,
            detail="Neighbor not found"
        )

    db.delete(neighbor)
    db.commit()

    return {"message": "Deleted"}


@router.put("/{neighbor_id}")
def update_neighbor(
    neighbor_id: int,
    data: NeighborUpdate,
    db: Session = Depends(get_db)
):
    neighbor = (
        db.query(Neighbor)
        .filter(Neighbor.id == neighbor_id)
        .first()
    )

    if not neighbor:
        raise HTTPException(
            status_code=404,
            detail="Neighbor not found"
        )

    neighbor.name = data.name
    neighbor.apartment = data.apartment
    neighbor.phone = data.phone

    db.commit()
    db.refresh(neighbor)

    return neighbor