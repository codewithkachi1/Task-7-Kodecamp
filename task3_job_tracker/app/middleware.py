from fastapi import Request, HTTPException

async def check_user_agent(request: Request, call_next):
    if "User-Agent" not in request.headers:
        raise HTTPException(status_code=400, detail="User-Agent header is missing")
    return await call_next(request)