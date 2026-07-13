# Q17. Create an undirected graph with the following edges:
# A - B, A - C, B - D, C - D
# Display the adjacency list of the graph.

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

for vertex in graph:
    print(vertex, "->", graph[vertex])