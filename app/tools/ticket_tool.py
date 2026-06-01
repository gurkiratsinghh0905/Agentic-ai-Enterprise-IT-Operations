import uuid

def create_ticket(issue):

    return {
        "ticket_id": str(uuid.uuid4())[:8],
        "issue": issue,
        "status": "OPEN"
    }