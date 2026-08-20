from pydantic import BaseModel, Field

class PaymentCreate(BaseModel):
    neighbor_id: int
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., ge=2020, le=2100)
    amount: float = Field(..., gt=0)
    paid: bool

class PaymentUpdate(BaseModel):
    neighbor_id: int
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., ge=2020, le=2100)
    amount: float = Field(..., gt=0)
    paid: bool