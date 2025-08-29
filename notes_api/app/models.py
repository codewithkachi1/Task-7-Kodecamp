from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))