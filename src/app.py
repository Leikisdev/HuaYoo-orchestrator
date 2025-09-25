from fastapi import FastAPI
from src.routes import dataRoute
from contextlib import asynccontextmanager
from httpx import AsyncClient
from src.utils.config import settings, Settings

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Instantiate settings - including HTTPX client
    settings = Settings(AsyncClient())
    yield
    
    # Clean up HTTPX client
    await settings.client.aclose()

app.include_router(dataRoute.dataRouter)
