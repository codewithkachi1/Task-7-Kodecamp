from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware import log_requests
from routers.students import student_router

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_requests)

app.include_router(student_router)