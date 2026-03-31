from fastapi import APIRouter
from backend.services.note_service import create_note, get_notes

router = APIRouter()

@router.post("/notes")
def add_note(user_id: str, content: str):
    note = create_note(user_id, content)
    return {"note": note}


@router.get("/notes")
def fetch_notes(user_id: str):
    return {"notes": get_notes(user_id)}