from sqlmodel import create_engine, Session
from models import Product

engine = create_engine("sqlite:///ecommerce.db")

def get_session():
    with Session(engine) as session:
        yield session
