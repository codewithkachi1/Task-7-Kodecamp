from fastapi import APIRouter, Depends, HTTPException
from models import Note
from database import get_session

note_router = APIRouter(prefix="/notes", tags=["notes"])

@note_router.post("/")
def create_note(note: Note, session=Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    # Save note to notes.json
    with open("notes.json", "a") as f:
        f.write(note.json() + "\n")
    return note

@note_router.get("/")
def read_notes(session=Depends(get_session)):
    notes = session.query(Note).all()
    return notes

@note_router.get("/{note_id}")
def read_note(note_id: int, session=Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@note_router.delete("/{note_id}")
def delete_note(note_id: int, session=Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"message": "Note deleted"}