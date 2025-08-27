from fastapi import APIRouter, Depends, HTTPException
from models import Student
from database import get_session
from auth import authenticate_user
from sqlmodel import select

student_router = APIRouter(prefix="/students", tags=["students"])

@student_router.post("/")
def create_student(student: Student, session=Depends(get_session), username: str = Depends(authenticate_user)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@student_router.get("/")
def read_students(session=Depends(get_session), username: str = Depends(authenticate_user)):
    students = session.exec(select(Student)).all()
    return students

@student_router.get("/{student_id}")
def read_student(student_id: int, session=Depends(get_session), username: str = Depends(authenticate_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@student_router.put("/{student_id}")
def update_student(student_id: int, student: Student, session=Depends(get_session), username: str = Depends(authenticate_user)):
    db_student = session.get(Student, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.age = student.age
    db_student.email = student.email
    db_student.grades = student.grades
    session.commit()
    session.refresh(db_student)
    return db_student

@student_router.delete("/{student_id}")
def delete_student(student_id: int, session=Depends(get_session), username: str = Depends(authenticate_user)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"message": "Student deleted"}
