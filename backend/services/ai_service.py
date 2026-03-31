import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt: str) -> str:
    """
    This function is responsible for interacting with the LLM (Ollama).

    WHY THIS EXISTS:
    - Keeps AI-related logic separate from API routes
    - Makes code reusable and testable
    - Follows clean architecture (service layer pattern)

    INPUT:
    - prompt: Fully prepared text (including context + user input)

    OUTPUT:
    - AI-generated response (string only)

    IMPORTANT:
    - This function does NOT handle memory
    - It ONLY talks to the model
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data.get("response", "")