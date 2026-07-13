# Q19. Perform a Breadth-First Search (BFS) traversal starting from vertex A.

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


def bfs(start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited


print("BFS starting from A:", bfs("A"))