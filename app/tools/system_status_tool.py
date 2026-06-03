from langchain_core.tools import tool


@tool
def get_system_status() -> dict:
    """Check the current status of enterprise IT services including VPN, mail, and network.
    Returns a dictionary with service names as keys and their status (UP/DOWN) as values."""
    return {
        "vpn": "UP",
        "mail": "UP",
        "network": "UP"
    }