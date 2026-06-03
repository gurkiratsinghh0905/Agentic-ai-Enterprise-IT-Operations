from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):

    # Core input/output
    query: str
    rewritten_query: str          # improved query (set to original when rewrite skipped)
    retrieved_docs: List          # list of plain text strings (not Document objects)
    sources: List[str]            # source filenames for citations
    diagnosis: str
    category: str                 # intent category from orchestrator
    tool_results: Dict[str, Any]
    resolution: str
    response: str

    # Control flow
    execution_path: List[str]
    monitoring: Dict[str, Any]
    need_tool: bool
    route: str
    retry_count: int              # tracks tool agent retry attempts
    error: str

    # Timing
    start_time: float             # workflow start timestamp for latency tracking