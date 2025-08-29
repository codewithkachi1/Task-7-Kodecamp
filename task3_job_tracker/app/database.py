from sqlmodel import create_engine, Session
from models import JobApplication

engine = create_engine("sqlite:///job_tracker.db")

def get_session():
    with Session(engine) as session:
        yield session