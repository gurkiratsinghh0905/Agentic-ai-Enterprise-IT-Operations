from typing import TypedDict

class AgentState(TypedDict):

    query:str

    retrieved_docs:list

    diagnosis:str

    tool_results:dict

    resolution:str

    response:str