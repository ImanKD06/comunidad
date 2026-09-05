from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from mangum import Mangum

from app.database.base import Base
from app.database.connection import engine

# Routers
from app.routers.actas import router as actas_router
from app.routers.communities import router as communities_router
from app.routers.expenses import router as expenses_router
from app.routers.incidents import router as incidents_router
from app.routers.neighbors import router as neighbors_router
from app.routers.payments import router as payments_router

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Community Manager API",
    version="1.0.0",
    redirect_slashes=False,
    lifespan=lifespan,
)




@app.middleware("http")
async def log_requests(request, call_next):
    print(f"INCOMING PATH: {request.url.path!r}")
    response = await call_next(request)
    print(f"RESPONSE STATUS: {response.status_code}")
    return response


# Registramos los routers
app.include_router(communities_router)
app.include_router(neighbors_router)
app.include_router(payments_router)
app.include_router(expenses_router)
app.include_router(incidents_router)
app.include_router(actas_router)


@app.get("/")
def root():
    return {"message": "Community Manager API running"}


handler = Mangum(app)