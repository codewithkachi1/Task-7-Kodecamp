from fastapi import APIRouter, Depends
from models import Product
from database import get_session
from auth import verify_token

product_router = APIRouter(prefix="/products", tags=["products"])

@product_router.post("/admin/")
def create_product(product: Product, session=Depends(get_session), username: str = Depends(verify_token)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@product_router.get("/")
def read_products(session=Depends(get_session)):
    products = session.query(Product).all()
    return products