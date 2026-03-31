from backend.services.ai_service import summarize_text

notes_db = {}

def create_note(user_id: str, content: str):
    """
    Store a new note and auto-generate summary.

    WHY:
    - Enhances user experience
    - Demonstrates AI + data integration
    """

    if user_id not in notes_db:
        notes_db[user_id] = []

    # Generate summary using AI
    summary = summarize_text(content)

    note = {
        "id": len(notes_db[user_id]) + 1,
        "content": content,
        "summary": summary
    }

    notes_db[user_id].append(note)

    return note


def get_notes(user_id: str):
    """
    Get all notes of a user.
    """
    return notes_db.get(user_id, [])