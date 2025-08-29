from sqlmodel import SQLModel, Field

class Contact(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: str
    user_id: int = Field(foreign_key="user.id")

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password: str