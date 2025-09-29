from fastapi import HTTPException
from src.utils.requestContext import RequestContext
from src.models.dbModels import *
import httpx

async def get_user(context: RequestContext):
    return await context.client.get(
        f"{context.config.ORM_BASE}/users/{context.user_token["uid"]}"
    )

async def create_user(user: UserCreate, context: RequestContext):
    try: 
        res = await context.config.client.post(
            f"{context.config.ORM_BASE}/users/",
            json = { 
                **user.model_dump(),
                'fedId': context.user_token["uid"],
            }
        )

        if res.status_code != httpx.codes.OK:
            raise HTTPException(status_code=404, detail="Unable to create user")

        return res.json()
    except Exception as e:
        print("An error occured:", e)
        raise HTTPException(status_code=404, detail="Unable to create user")

