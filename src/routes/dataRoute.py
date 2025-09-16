from fastapi import APIRouter, Depends
import httpx
from utils.requestContext import RequestContext, get_req_context

dataRouter = APIRouter()

@dataRouter.get("/users/")
async def read_users(context: RequestContext = Depends(get_req_context)):
    async with httpx.AsyncClient() as client:
        return [{"username": "Rick"}, {"username": "Morty"}]


@dataRouter.post("/users/")
async def create_user(context: RequestContext = Depends(get_req_context)):
    return [{"username": "Rick"}, {"username": "NewMorty"}]