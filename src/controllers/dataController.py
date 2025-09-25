from fastapi import HTTPException
from src.utils.requestContext import RequestContext
from src.utils.config import settings
from firebase_admin import auth
from src.models.dbModels import *

async def get_user(context: RequestContext):
    return await context.client.get(
        f"{settings.orm_base}/users/{context.user_token["uid"]}"
    )

async def create_user(user: UserCreate,context: RequestContext):
    try: 
        current_user = auth.get_user(context.user_token["uid"])
        huayoo_user = { 
            'email': current_user.email, 
            'username': current_user.displayName,
            'fedId': current_user.uid
        }
        
        return await context.client.post(
            f"{settings.orm_base}/users/",
            data = huayoo_user
        )
    except Exception as e:
        print("An error occured:", e)
        raise HTTPException(status_code=404, detail="Unable to create user")

