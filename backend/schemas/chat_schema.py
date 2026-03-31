from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Defines input structure for chat endpoint.
    Ensures clean validation and readability.
    """
    user_id: str
    prompt: str