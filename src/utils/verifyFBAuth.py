import firebase_admin
from firebase_admin import auth
from fastapi import HTTPException
from typing import Optional

# Only initialize once
if not firebase_admin._apps:
    firebase_admin.initialize_app()
        
def verify_auth(authorization: Optional[str] = None):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Missing or invalid Authorization header")
    
    try:
        decoded_token = auth.verify_id_token(authorization.split(" ")[1])
        return decoded_token
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")
