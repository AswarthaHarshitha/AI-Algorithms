import heapq
from collections import deque
# Graph Representation
graph = {
    0: {1: 3, 3: 8, 4: 7},
    1: {0: 3, 3: 4, 2: 1},
    2: {1: 1, 3: 2},
    3: {0: 8, 1: 4, 2: 2, 4: 3},
    4: {0: 7, 3: 3}
}
# Problem 1: Dijkstra's Algorithm (Shortest Path)
def dijkstra(graph, start, target):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == target:
            break
        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))
    # Reconstruct shortest path
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    return " -> ".join(map(str, path[::-1])), distances[target]
# Problem 2: BFS Traversal
def bfs(graph, start):
    queue, visited = deque([start]), set()
    bfs_order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            queue.extend(graph[node])
    
    return " -> ".join(map(str, bfs_order))
# Problem 3: DFS Traversal
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return " -> ".join(map(str, dfs_order))
# Problem 4: Cycle Detection
def detect_cycle(graph):
    visited, rec_stack = set(), set()
    
    def dfs(node, parent):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor in rec_stack and neighbor != parent:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return "Cycle Detected"
    return "No Cycle Detected"
# Problem 5: Graph Coloring
def color_graph(graph):
    colors, available_colors = {}, ['Red', 'Green', 'Blue']
    
    for node in graph:
        used_colors = {colors[neighbor] for neighbor in graph[node] if neighbor in colors}
        for color in available_colors:
            if color not in used_colors:
                colors[node] = color
                break
    
    return colors
# Running All Problems
shortest_path, cost = dijkstra(graph, 0, 2)
print(f"Shortest Path: {shortest_path}, Cost: {cost}")
print(f"BFS Traversal: {bfs(graph, 0)}")
dfs_order = []
print(f"DFS Traversal: {dfs(graph, 0)}")
print(f"Cycle Detection: {detect_cycle(graph)}")
print("Node Coloring:", color_graph(graph))
