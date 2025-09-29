from typing import Any
from httpx import AsyncClient
from fastapi import Depends, Header
from typing import Optional
import src.utils.config as config
from src.utils.verifyFBAuth import verify_auth


class RequestContext:
    config: config.Settings
    user_token: Any

    def __init__(self, config: config.Settings, decoded_token: Any):
        self.config = config
        self.user_token = decoded_token

def get_req_context(
    authorization: Optional[str] = Header(None),
    config: config.Settings = Depends(config.get_settings),
) -> RequestContext: 
    return RequestContext(config, verify_auth(authorization))