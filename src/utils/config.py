from pydantic_settings import BaseSettings
from pydantic import Field
from httpx import AsyncClient
from functools import cache

class Settings(BaseSettings):
    # Overwritten from .env file if applicable
    ENV: str = "development"
    ORM_BASE: str = "http://localhost:3000"
    AI_URL: str = "http://localhost:5000"
    
    # runtime-only client, created automatically and ignored by basesetting .env file handling
    client: AsyncClient = Field(default_factory=lambda: AsyncClient(), exclude=True)

    class Config:
        env_file = ".env"
        extra = "allow"

# Caches settings so they are only set up once
@cache
def get_settings() -> Settings:
    return Settings()