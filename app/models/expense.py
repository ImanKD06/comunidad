from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from app.database.base import Base

class Expense(Base):
    __tablename__ = "EXPENSES"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String(255))

    amount = Column(DECIMAL(10, 2))

    date = Column(Date)

    community_id = Column(
        Integer,
        ForeignKey("COMMUNITIES.id", ondelete="CASCADE", onupdate="CASCADE")
    )