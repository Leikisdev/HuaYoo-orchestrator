from fastapi import FastAPI
from src.routes import dataRoute
from contextlib import asynccontextmanager
import src.utils.config as config
from dotenv import load_dotenv
import os

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Setting up app")
    yield
    
    # Clean up HTTPX client
    await config.get_settings().client.aclose()

app = FastAPI(lifespan=lifespan)
app.include_router(dataRoute.dataRouter)

# If frontend is running as web app, CORS handling is needed
if os.environ['PLATFORM'] == 'web':
    print("Setting up CORS")
    from fastapi.middleware.cors import CORSMiddleware
    origins = [
        "http://localhost:8081",  # Expo web
        "http://127.0.0.1:8081",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
