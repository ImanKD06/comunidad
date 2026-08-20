from sqlalchemy import Column, Integer, String, Text, Date
from app.database.base import Base

class Actas(Base):
    __tablename__ = "actas"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    meeting_date = Column(Date)
    attendees = Column(Text)
    topics = Column(Text)
    agreements = Column(Text)
    content = Column(Text)
    community_id = Column(Integer)