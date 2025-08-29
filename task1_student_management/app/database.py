from sqlmodel import create_engine, Session
from models import Student

engine = create_engine("sqlite:///student.db")

def get_session():
    with Session(engine) as session:
        yield session
