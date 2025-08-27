from fastapi import APIRouter, Depends, HTTPException
from models import Student
from database import get_session
from auth import authenticate_user
from sqlmodel import select

student_router = APIRouter(prefix="/students", tags=["students"])

