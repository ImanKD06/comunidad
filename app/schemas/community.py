from pydantic import BaseModel


class CommunityCreate(BaseModel):
    name: str
    address: str


class CommunityUpdate(BaseModel):
    name: str
    address: str