from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start_node):
    
    visited = set([start_node])
    queue = deque([start_node])

    while queue:
       
        vertex = queue.popleft()
        print(vertex, end=" ")

      
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("BFS Traversal starting from 'A':")
bfs(graph, 'A')