import os
from dotenv import load_dotenv
from httpx import AsyncClient

ENV = os.getenv("ENV", "development")
if ENV == "development":
    load_dotenv()

class Settings:
    def __init__(self, client: AsyncClient):
        self.env = ENV
        self.client = client

        if self.env == "development":
            # Localhost URLs
            self.orm_base = "http://localhost:3000"
            self.ai_url = "http://localhost:5000"
        else:
            # Production URLs
            self.orm_base = f"http://{os.getenv("ORM_BASE")}"
            self.ai_url = f"https://{os.getenv("AI_URL")}"

settings: Settings | None = None