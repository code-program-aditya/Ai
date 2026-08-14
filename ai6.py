import heapq
from os import path
from platform import node
graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F'],
    'D':['G'],
    'E':['G'],
    'F':['G'],
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
            if nbr not in visited:
                heapq.heappush(pq, (heuristic[nbr], g + cost, nbr, path + [nbr]))
    return None

result = astar('A', 'G')
print(result)