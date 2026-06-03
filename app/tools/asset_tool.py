from langchain_core.tools import tool


@tool
def asset_lookup(user: str) -> dict:
    """Look up the IT asset (device) assigned to a given employee.
    Returns employee name, device model, and serial number."""
    return {
        "employee": user,
        "device": "Dell Latitude",
        "serial": "DL123456"
    }
