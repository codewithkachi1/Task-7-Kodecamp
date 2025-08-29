from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from jose import jwt
from models import User
from database import get_session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = "secret_key_here"

security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), session=Depends(get_session)):
    user = session.query(User).filter(User.username == credentials.username).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.id}, SECRET_KEY, algorithm="HS256")
    return {"token": token}

@auth_router.post("/login")
def login(username: str, password: str, session=Depends(get_session)):
    user = session.query(User).filter(User.username == username, User.password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.id}, SECRET_KEY, algorithm="HS256")
    return {"token": token}