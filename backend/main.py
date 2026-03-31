from fastapi import FastAPI
import requests
from backend.services.memory import get_history, add_message
from backend.services.ai_service import generate_response
from backend.services.ai_service import summarize_text
from backend.routes.chats import router as chat_router
from backend.routes.summerize import router as summarize_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(summarize_router)