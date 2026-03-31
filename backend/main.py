from fastapi import FastAPI
import requests
from backend.services.memory import get_history, add_message
from backend.services.ai_service import generate_response
from backend.services.ai_service import summarize_text

app = FastAPI()

@app.post("/chat")
def chat(user_id: str, prompt: str):
    """
    This endpoint handles a conversation with memory.

    IMPORTANT CONCEPT:
    - LLMs (like Llama3) DO NOT remember anything on their own.
    - We manually create "memory" by sending previous conversation
      along with the new prompt every time.

    Flow:
    1. Get past conversation (memory)
    2. Convert it into text (context)
    3. Append current user input
    4. Send everything to LLM
    5. Save new messages back into memory
    """

    # Step 1: Fetch past conversation for this user
    # If user is new → returns empty list
    history = get_history(user_id)

    # Step 2: Convert history into a single text prompt
    # This is how we "inject memory" into LLM
    context = ""
    for msg in history:
        context += f"{msg['role']}: {msg['content']}\n"

    # Step 3: Add current user input
    # We end with "assistant:" so model continues from there
    full_prompt = context + f"user: {prompt}\nassistant:"

    # Step 4: Send request to Ollama (LLM) and get response
    ai_response = generate_response(full_prompt)

    # Step 5: Save both user + AI messages in memory
    # So next request includes this conversation
    add_message(user_id, "user", prompt)
    add_message(user_id, "assistant", ai_response)

    # ⚠️ LIMITATION:
    # - This memory is stored in RAM (Python dictionary)
    # - If server restarts → memory is lost
    # - Next step: store in database (PostgreSQL / Redis)

    return {
        "response": ai_response
    }

@app.post("/summarize")
def summarize(text: str):
    """
    Generates a concise summary of the given text.

    This is a dedicated endpoint for summarization, separate from chat.
    """

    summary = summarize_text(text)

    return {
        "summary": summary
    }