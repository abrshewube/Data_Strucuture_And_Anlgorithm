#Breadth-First Search (BFS) Implementation:

from collections import deque

def bfs(graph,start):
    queue=deque([start])
    visted=set([start])
    while queue:
        vertex=queue.popleft()
        print(f"visting {vertex}")
        # Enqueue all unvisited neighbors
        for neighbour in graph[vertex]:
            if neighbour not in visted:
                queue.append(neighbour)
                visted.add(neighbour)
                
                
                
                
                
# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['B']
}


print("BFS Traversal:")
bfs(graph, 'E')