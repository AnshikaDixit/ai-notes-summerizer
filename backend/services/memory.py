# backend/services/memory.py

chat_memory = {}

def get_history(user_id: str): # Give me all past messages of this user, If no history → return empty list
    return chat_memory.get(user_id, [])

def add_message(user_id: str, role: str, content: str): 
    # Save message in memory
    # Example stored:
    # [
    #   {"role": "user", "content": "My name is Anshika"},
    #   {"role": "assistant", "content": "Nice to meet you"}
    # ]

    if user_id not in chat_memory:
        chat_memory[user_id] = []
    
    chat_memory[user_id].append({
        "role": role,
        "content": content
    })

