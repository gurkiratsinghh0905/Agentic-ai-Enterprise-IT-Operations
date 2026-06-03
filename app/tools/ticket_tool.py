import uuid
from langchain_core.tools import tool


@tool
def create_ticket(issue: str) -> dict:
    """Create a new IT support ticket for the given issue description.
    Returns a ticket dictionary with ticket_id, issue description, and status OPEN."""
    return {
        "ticket_id": str(uuid.uuid4())[:8],
        "issue": issue,
        "status": "OPEN"
    }