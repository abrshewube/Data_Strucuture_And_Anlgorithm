def dfs(graph,start):
    visted=set()
    def helper(vertex):
        visted.add(vertex)
        print(f"visted {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visted:
                helper(neighbour)
    helper(start)
    
    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['B']
}

# Starting DFS from vertex 'A'
print("DFS Traversal:")
dfs(graph, 'B')