from state import AgentState
from tools.calculator import calculator
from langchain_community.llms import Ollama
from rag import retrieve

llm = Ollama(model="llama3")


def decision_node(state: AgentState) -> AgentState:
    query = state["query"]

    if any(char.isdigit() for char in query):
        state["decision"] = "tool"
    elif "contract" in query.lower():
        state["decision"] = "retrieval"
    else:
        state["decision"] = "direct"

    return state


def tool_node(state: AgentState) -> AgentState:
    state["tool_output"] = calculator(state["query"])
    return state


def retrieval_node(state: AgentState) -> AgentState:
    context = retrieve(state["query"])
    state["retrieved_docs"] = context
    return state


def llm_node(state: AgentState) -> AgentState:
    if state["decision"] == "tool":
        prompt = f"Tool result: {state['tool_output']}"

    elif state["decision"] == "retrieval":
        prompt = f"""
        Use this context:
        {state['retrieved_docs']}

        Question: {state['query']}
        """

    else:
        prompt = state["query"]

    state["response"] = llm.invoke(prompt)
    return state


def evaluation_node(state: AgentState) -> AgentState:
    response = state["response"]

    state["evaluation"] = {
        "response_length": len(response),
        "has_context": state.get("retrieved_docs") is not None
    }

    return state
