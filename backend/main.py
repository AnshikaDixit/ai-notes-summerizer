from fastapi import FastAPI
import requests
from backend.services.memory import get_history, add_message

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def home():
    return {"message": "AI Notes Backend Running 🚀"}

@app.post("/generate")
def generate(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return {
        "response": data.get("response", "")
    }

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

    # Step 4: Send request to Ollama (LLM)
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    # Step 5: Extract AI response
    data = response.json()
    ai_response = data.get("response", "")

    # Step 6: Save both user + AI messages in memory
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