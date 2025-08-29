from fastapi import APIRouter, Depends, HTTPException
from models import Contact
from database import get_session
from security import get_current_user

contact_router = APIRouter(prefix="/contacts", tags=["contacts"])

@contact_router.post("/")
def create_contact(contact: Contact, session=Depends(get_session), user=Depends(get_current_user)):
    contact.user_id = user.id
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return contact

@contact_router.get("/")
def read_contacts(session=Depends(get_session), user=Depends(get_current_user)):
    contacts = session.query(Contact).filter(Contact.user_id == user.id).all()
    return contacts

@contact_router.put("/{contact_id}")
def update_contact(contact_id: int, contact: Contact, session=Depends(get_session), user=Depends(get_current_user)):
    db_contact = session.get(Contact, contact_id)
    if not db_contact or db_contact.user_id != user.id:
        raise HTTPException(status_code=404, detail="Contact not found")
    db_contact.name = contact.name
    db_contact.email = contact.email
    db_contact.phone = contact.phone
    session.commit()
    session.refresh(db_contact)
    return db_contact

@contact_router.delete("/{contact_id}")
def delete_contact(contact_id: int, session=Depends(get_session), user=Depends(get_current_user)):
    contact = session.get(Contact, contact_id)
    if not contact or contact.user_id != user.id:
        raise HTTPException(status_code=404, detail="Contact not found")
    session.delete(contact)
    session.commit()
    return {"message": "Contact deleted"}