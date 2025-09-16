from typing import Any
from httpx import AsyncClient
from fastapi import Header
from typing import Optional
from app import get_client
from verifyFBAuth import verify_auth

class RequestContext:
    client: AsyncClient
    user_token: Any

    def __init__(self, client: AsyncClient, decoded_token: Any):
        self.client = client
        self.user_token = decoded_token

def get_req_context(authorization: Optional[str] = Header(None)) -> RequestContext: 
    return RequestContext(
        get_client(),
        verify_auth(authorization)
    )