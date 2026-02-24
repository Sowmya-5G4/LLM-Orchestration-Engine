from graph import graph


def run_agent(query: str):
    state = {
        "query": query,
        "decision": None,
        "tool_output": None,
        "retrieved_docs": None,
        "response": None,
        "memory_context": None,
        "evaluation": None
    }

    result = graph.invoke(state)
    return result


if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        output = run_agent(q)
        print("\nResponse:\n", output["response"])
        print("\nEvaluation:\n", output["evaluation"])
