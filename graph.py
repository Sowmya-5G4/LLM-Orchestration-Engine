from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import decision_node, tool_node, retrieval_node, llm_node, evaluation_node


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("decision", decision_node)
    builder.add_node("tool", tool_node)
    builder.add_node("retrieval", retrieval_node)
    builder.add_node("llm", llm_node)
    builder.add_node("evaluation", evaluation_node)

    builder.set_entry_point("decision")

    builder.add_conditional_edges(
        "decision",
        lambda state: state["decision"],
        {
            "tool": "tool",
            "retrieval": "retrieval",
            "direct": "llm"
        }
    )

    builder.add_edge("tool", "llm")
    builder.add_edge("retrieval", "llm")
    builder.add_edge("llm", "evaluation")
    builder.add_edge("evaluation", END)

    return builder.compile()


graph = build_graph()
