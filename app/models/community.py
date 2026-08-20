
from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Community(Base):
    __tablename__ = "COMMUNITIES"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255))
