from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(graph[node]- visited)
    return traversal
graph ={
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print("BFS Traversal:", bfs(graph, 'A'))
