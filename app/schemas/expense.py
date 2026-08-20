from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    date: date
    community_id: int


class ExpenseUpdate(BaseModel):
    description: str
    amount: float
    date: date
    community_id: int