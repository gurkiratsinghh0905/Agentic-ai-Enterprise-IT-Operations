from typing import TypedDict
from typing import List
from typing import Dict
from typing import Any


class AgentState(TypedDict):

    query: str

    retrieved_docs: List

    diagnosis: str

    tool_results: Dict[str, Any]

    resolution: str

    response: str

    execution_path: List[str]

    monitoring: Dict[str, Any]

    need_tool: bool

    route: str

    error: str