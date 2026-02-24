import json


MEMORY_FILE = "memory.json"


def save_memory(query, response):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({"query": query, "response": response})

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []
