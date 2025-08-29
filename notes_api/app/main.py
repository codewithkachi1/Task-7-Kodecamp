from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware import count_requests
from routers.notes import note_router

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(count_requests)

app.include_router(note_router)