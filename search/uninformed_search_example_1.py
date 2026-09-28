from collections import deque
import heapq
graph = {
    'a': {'b': 9, 'c': 4, 'd': 7},
    'b': {'e': 11},
    'c': {'e': 17, 'f': 12},
    'd': {'f': 14},
    'e': {'z': 5},
    'f': {'z': 9},
    'z': {}
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
    path = []
    node = target
    while node:
        path.append(node)
        node = parent[node]
    return " -> ".join(path[::-1]), distances[target]
# Problem 2: BFS
def bfs(graph, start):
    queue, visited = deque([start]), set()
    bfs_order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            queue.extend(graph[node])
    return " -> ".join(bfs_order)
# Problem 3: DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return " -> ".join(dfs_order)
# Problem 4: Cycle Detection
def detect_cycle(graph):
    visited, rec_stack = set(), set()
    def dfs(node):
        if node in rec_stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        rec_stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
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
# Running all problems
shortest_path, cost = dijkstra(graph, 'a', 'z')
print(f"1. Shortest Path: {shortest_path}, Cost: {cost}")
print(f"2. BFS: {bfs(graph, 'a')}")
dfs_order = []
print(f"3. DFS: {dfs(graph, 'a')}")
print(f"4. Cycle Detection: {detect_cycle(graph)}")
print("5. Node Coloring:", color_graph(graph))
