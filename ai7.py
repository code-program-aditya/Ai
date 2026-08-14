import heapq
graph = {
    'A':[('B', 1), ('C', 4)],
    'B':[('D', 2), ('E', 5)],
    'C':[('F', 2)],
    'D':[('G', 4)],
    'E':[('G', 2)],
    'F':[('G', 1)],
    'G':[]
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0, 'F': 3, 'G': 0}
def astar(start, goal):
    pq=[]
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))
    visited = set()
    while pq:
        h, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for nbr, cost in graph[node]:
            new_g = g + cost
            new_h = heuristic[nbr]
            heapq.heappush(pq, (new_h, new_g, nbr, path + [nbr]))
    return None
    
result = astar('A', 'G')
print(result)