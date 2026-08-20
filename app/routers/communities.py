from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.community import Community
from app.schemas.community import CommunityCreate, CommunityUpdate


router = APIRouter(prefix="/communities", tags=["Communities"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_communities(db: Session = Depends(get_db)):
    return db.query(Community).all()



@router.post("/")
def create_community(
    community: CommunityCreate, 
    db: Session = Depends(get_db)
    ):

    new_community = Community(
        name=community.name,
        address=community.address
    )

    db.add(new_community)
    db.commit()
    db.refresh(new_community)

    return new_community


@router.delete("/{community_id}")
def delete_community(
    community_id: int,  
    db: Session = Depends(get_db)
    ):

    community = db.query(Community).filter(Community.id == community_id).first()

    if not community:
        raise HTTPException(status_code=404, detail="Community not found")

    db.delete(community)
    db.commit()

    return {"message": "Deleted"}



@router.put("/{community_id}")
def update_community(
    community_id: int,
    data: CommunityUpdate,
    db: Session = Depends(get_db)
):
    community = (
    db.query(Community)
    .filter(Community.id == community_id)
    .first()
)

    if not community:
        raise HTTPException(status_code=404, detail="Community not found")

    community.name = data.name
    community.address = data.address

    db.commit()
    db.refresh(community)

    return community