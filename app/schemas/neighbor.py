from pydantic import BaseModel, Field

class NeighborCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    apartment: str = Field(..., min_length=1, max_length=20)
    phone: str = Field(..., min_length=9, max_length=15)
    community_id: int

class NeighborUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    apartment: str = Field(..., min_length=1, max_length=20)
    phone: str = Field(..., min_length=9, max_length=15)
    community_id: int

