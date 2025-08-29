from fastapi import APIRouter, Depends
from models import JobApplication
from database import get_session
from auth import verify_token

application_router = APIRouter(prefix="/applications", tags=["applications"])

@application_router.post("/")
def create_application(application: JobApplication, session=Depends(get_session), user_id: int = Depends(verify_token)):
    application.user_id = user_id
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

@application_router.get("/")
def read_applications(session=Depends(get_session), user_id: int = Depends(verify_token)):
    applications = session.query(JobApplication).filter(JobApplication.user_id == user_id).all()
    return applications

@application_router.get("/search")
def search_applications(status: str, session=Depends(get_session), user_id: int = Depends(verify_token)):
    applications = session.query(JobApplication).filter(JobApplication.user_id == user_id, JobApplication.status == status).all()
    return applications
