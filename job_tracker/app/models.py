from sqlmodel import SQLModel, Field

class JobApplication(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    company: str
    position: str
    status: str
    date_applied: str
    user_id: int = Field(foreign_key="user.id")