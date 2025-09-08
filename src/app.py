from auth import verifyFBAuth
from fastapi import Depends, FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()
auth_verifier = verifyFBAuth.VerifyFBAuth()

def verify_auth(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Missing or invalid Authorization header")
    
    current_user = auth_verifier.verify_token(authorization.split(" ")[1])

    if current_user is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return current_user

@app.get("/users/")
async def read_users(current_user: dict = Depends(verify_auth)):
    return [{"username": "Rick"}, {"username": "Morty"}]


@app.post("/users/")
async def create_user(current_user: dict = Depends(verify_auth)):
    return [{"username": "Rick"}, {"username": "NewMorty"}]
