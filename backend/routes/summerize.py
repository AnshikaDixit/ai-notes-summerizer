from fastapi import APIRouter
from services.ai_service import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize(text: str):
    """
    Generates a concise summary of the given text.

    This is a dedicated endpoint for summarization, separate from chat.
    """

    summary = summarize_text(text)

    return {
        "summary": summary
    }