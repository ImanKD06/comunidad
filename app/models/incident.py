from sqlalchemy import Column, Integer, String, Text, Date
from app.database.base import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    status = Column(String(50))
    priority = Column(String(50))
    created_at = Column(Date)
    community_id = Column(Integer)