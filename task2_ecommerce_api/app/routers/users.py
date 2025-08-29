from fastapi import APIRouter, Depends
from auth import generate_token

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/login/")
def login(username: str, password: str):
    # Login logic
    token = generate_token(username)
    return {"token": token}
