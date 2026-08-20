from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.connection import engine

from app.models.community import Community
from app.models.neighbor import Neighbor
from app.models.payment import Payment
from app.models.expense import Expense
from app.models.actas import Actas
from app.models.incident import Incident
from app.routers import ai

from app.routers import (
    communities,
    neighbors,
    payments,
    expenses,
    actas,
    incidents,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(communities.router)
app.include_router(neighbors.router)
app.include_router(payments.router)
app.include_router(expenses.router)
app.include_router(actas.router)
app.include_router(incidents.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}