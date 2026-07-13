# Q18. Check whether there is a direct edge between two given vertices.

graph = {}


def add_edge(a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)


add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")


def has_edge(a, b):
    return a in graph and b in graph[a]


print("Edge between A and D:", has_edge("A", "D"))
print("Edge between A and B:", has_edge("A", "B"))