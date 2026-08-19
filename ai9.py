"""Module docstring."""
import heapq
graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':['G'],
'E':['G'],
'F':['G'],
'G':[]
}
heuristic={'A':7,'B':6,'C':4,'D':3,'E':2,'F':1,'G':0}
def best_first_search(start,goal):
    pq=[]
    heapq.heappush(pq,(heuristic[start],start,[start]))
    visited=set()
    while pq:
        h,node,path=heapq.heappop(pq)
        if node==goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                heapq.heappush(pq,(heuristic[nbr],nbr,path+[nbr]))
    return None

print(best_first_search('A','G'))