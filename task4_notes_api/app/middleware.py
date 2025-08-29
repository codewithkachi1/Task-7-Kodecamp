from fastapi import Request
import logging
import json

request_count = 0

logging.basicConfig(filename="requests.log", level=logging.INFO)

async def count_requests(request: Request, call_next):
    global application
    global request_count
    request_count += 1
    logging.info(f"Request {request_count}: {request.method} {request.url}")
    response = await call_next(request)
    return response