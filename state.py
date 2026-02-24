from typing import TypedDict, Optional, Dict


class AgentState(TypedDict):
    query: str
    decision: Optional[str]
    tool_output: Optional[str]
    retrieved_docs: Optional[str]
    response: Optional[str]
    memory_context: Optional[str]
    evaluation: Optional[Dict]

