from pydantic import BaseModel

class NoteRequest(BaseModel):
    text: str

class NoteResponse(BaseModel):
    summary: str