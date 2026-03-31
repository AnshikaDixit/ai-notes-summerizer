"""
Central configuration file.

WHY:
- Avoid hardcoding values across files
- Easy to change environment (dev/prod)
- Cleaner architecture
"""

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3"