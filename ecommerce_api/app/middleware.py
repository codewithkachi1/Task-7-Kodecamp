from fastapi import Request
import time

async def measure_response_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    response_time = end_time - start_time
    response.headers["X-Response-Time"] = str(response_time)
    return response
