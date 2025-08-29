from sqlmodel import SQLModel, Field

class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
    grades: str
