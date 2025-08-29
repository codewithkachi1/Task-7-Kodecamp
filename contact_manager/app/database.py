from sqlmodel import create_engine, Session
from models import Contact, User

engine = create_engine("sqlite:///contact_manager.db")

def get_session():
    with Session(engine) as session:
        yield session