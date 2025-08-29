from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware import measure_response_time
from routers.products import product_router
from routers.cart import cart_router
from routers.users import user_router

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(measure_response_time)

app.include_router(product_router)
app.include_router(cart_router)
app.include_router(user_router)
