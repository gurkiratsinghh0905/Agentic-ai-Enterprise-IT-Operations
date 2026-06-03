from langchain_core.tools import tool


@tool
def software_lookup(name: str) -> str:
    """Check whether a specific software application is approved for enterprise use.
    Returns 'approved' or 'not approved' for the given software name."""
    approved = {
        "zoom": "approved",
        "teams": "approved",
        "chrome": "approved",
        "slack": "approved",
        "vscode": "approved",
    }
    return approved.get(name.lower(), "not approved")
