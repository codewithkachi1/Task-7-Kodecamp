from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
import hashlib

security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    with open("users.json", "r") as f:
        users = json.load(f)
    user = users.get(credentials.username)
    if not user or user["password"] != hashlib.sha256(credentials.password.encode()).hexdigest():
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username