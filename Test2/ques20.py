# Q20. Perform a Depth-First Search (DFS) traversal starting from vertex A.

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


def dfs(start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited


print("DFS starting from A:", dfs("A"))