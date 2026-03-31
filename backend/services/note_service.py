notes_db = {}

def create_note(user_id: str, content: str):
    """
    Store a new note for a user.
    """

    if user_id not in notes_db:
        notes_db[user_id] = []

    note = {
        "id": len(notes_db[user_id]) + 1,
        "content": content
    }

    notes_db[user_id].append(note)

    return note


def get_notes(user_id: str):
    """
    Get all notes of a user.
    """
    return notes_db.get(user_id, [])