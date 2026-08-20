from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Neighbor(Base):
    __tablename__ = "NEIGHBORS"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    apartment = Column(String(50))
    phone = Column(String(20))

    community_id = Column(
        Integer,
        ForeignKey("COMMUNITIES.id", ondelete="CASCADE", onupdate="CASCADE")
    )