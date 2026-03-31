from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    """
    Input schema for summarization.
    """
    text: str