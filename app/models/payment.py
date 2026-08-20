from sqlalchemy import Column, Integer, DECIMAL, Boolean, ForeignKey, CheckConstraint
from app.database.base import Base

class Payment(Base):
    __tablename__ = "PAYMENTS"

    id = Column(Integer, primary_key=True, index=True)

    neighbor_id = Column(
    Integer,
    ForeignKey("NEIGHBORS.id", ondelete="CASCADE", onupdate="CASCADE"),
    nullable=False
)

    month = Column(Integer)
    year = Column(Integer)

    amount = Column(DECIMAL(10, 2))

    paid = Column(Boolean, default=False)

    __table_args__ = (
        CheckConstraint('month >= 1 AND month <= 12', name='check_month'),
    )