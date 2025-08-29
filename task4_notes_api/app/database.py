from sqlmodel import create_engine, Session
from models import Note

engine = create_engine("sqlite:///notes.db")

def get_session():
    with Session(engine) as session:
        yield session