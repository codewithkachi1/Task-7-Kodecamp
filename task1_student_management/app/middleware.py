import logging
from fastapi import Request
from datetime import datetime

logging.basicConfig(filename="logs/log_file.log", level=logging.INFO)

async def log_requests(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    end_time = datetime.now()
    logging.info(f"{request.method} {request.url} {response.status_code} {end_time - start_time}")
    return response