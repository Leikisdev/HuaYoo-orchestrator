from fastapi import APIRouter, Depends
from src.utils.requestContext import RequestContext, get_req_context
from src.controllers import dataController as controller
from src.models.dbModels import *

dataRouter = APIRouter()

@dataRouter.get("/users/")
async def read_users(context: RequestContext = Depends(get_req_context)):
    return await controller.get_user(context)


@dataRouter.post("/users/")
async def create_user(
    user: UserCreate,
    context: RequestContext = Depends(get_req_context),
):
    print(f"Creating user {user}")
    return await controller.create_user(user, context)