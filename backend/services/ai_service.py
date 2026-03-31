import requests
from backend.core.config import OLLAMA_URL, MODEL_NAME

# def generate_response(prompt: str) -> str:
#     """
#     This function is responsible for interacting with the LLM (Ollama).

#     WHY THIS EXISTS:
#     - Keeps AI-related logic separate from API routes
#     - Makes code reusable and testable
#     - Follows clean architecture (service layer pattern)

#     INPUT:
#     - prompt: Fully prepared text (including context + user input)

#     OUTPUT:
#     - AI-generated response (string only)

#     IMPORTANT:
#     - This function does NOT handle memory
#     - It ONLY talks to the model
#     """

#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": "llama3",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     data = response.json()

#     return data.get("response", "")

def generate_response(prompt: str) -> str:
    """
    Handles interaction with LLM.

    Now includes a SYSTEM PROMPT to control behavior.
    """

    # System prompt = defines AI behavior
    system_prompt = """
    You are an AI Notes Assistant.

    Rules:
    - Give short and clear answers
    - Prefer bullet points when possible
    - If asked to summarize, provide concise summary
    - Do not give unnecessary explanations
    """

    # Combine system + user prompt
    final_prompt = system_prompt + "\n" + prompt

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": final_prompt,
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "")


def summarize_text(text: str) -> str:
    """
    Generates a concise summary of given text.

    WHY:
    - Core feature of AI Notes app
    - Uses LLM with summarization-focused prompt
    """

    prompt = f"""
    You are a notes summarizer.

    Summarize the following text in a concise and clear way:

    {text}
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