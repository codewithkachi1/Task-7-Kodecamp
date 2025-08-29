from fastapi import Request
import logging

logging.basicConfig(filename="requests.log", level=logging.INFO)

async def log_ip_address(request: Request, call_next):
    ip_address = request.client.host
    logging.info(f"Request from IP address: {ip_address}")
    response = await call_next(request)
    return response