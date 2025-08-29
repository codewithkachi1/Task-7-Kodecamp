from fastapi import APIRouter, Depends, HTTPException
from models import Product
from database import get_session
from auth import verify_token

cart_router = APIRouter(prefix="/cart", tags=["cart"])

@cart_router.post("/add/")
def add_to_cart(product_id: int, quantity: int, session=Depends(get_session), username: str = Depends(verify_token)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Add product to cart
    return {"message": "Product added to cart"}

@cart_router.post("/checkout/")
def checkout(session=Depends(get_session), username: str = Depends(verify_token)):
    # Checkout logic
    return {"message": "Checkout successful"}
