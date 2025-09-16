from fastapi import Depends, FastAPI, Header, HTTPException
from routes import dataRoute
from contextlib import asynccontextmanager
import httpx

app = FastAPI()
client: httpx.AsyncClient | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Instantiate httpx client
    global client
    client = httpx.AsyncClient()
    yield
    
    # Clean up HTTPX client
    await client.aclose()

app.include_router(dataRoute.dataRouter)

# Dependency getter
def get_client() -> httpx.AsyncClient:
    return client
