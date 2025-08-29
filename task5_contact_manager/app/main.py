from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.contacts import contact_router
from routers.auth import auth_router
from middleware import log_ip_address

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_ip_address)

app.include_router(contact_router)
app.include_router(auth_router)