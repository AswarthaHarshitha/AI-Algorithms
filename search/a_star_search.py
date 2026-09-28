graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 1)],
    'G': []
}

heuristic = {
    'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0
}

def find_min_f(open_list, g_values):
    """Finds the node in open_list with the lowest f = g + h value."""
    min_node = open_list[0]
    min_f = g_values.get(min_node, float('inf')) + heuristic.get(min_node, float('inf'))

    for node in open_list:
        f_value = g_values.get(node, float('inf')) + heuristic.get(node, float('inf'))
        if f_value < min_f:
            min_f = f_value
            min_node = node

    return min_node

def a_star(start, goal):
    open_list = [start]   # Nodes to explore
    closed_list = set()   # Explored nodes

    g_values = {start: 0}  # Cost from start to each node
    parent = {start: None} # To track the path

    while open_list:
        current = find_min_f(open_list, g_values)
        open_list.remove(current)
        closed_list.add(current)

        print(f"Visiting: {current}")

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Goal Reached!")
            print("Path:", " -> ".join(path))
            print("Cost:", g_values[goal])
            return

        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_values[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= g_values.get(neighbor, float('inf')):
                continue

            parent[neighbor] = current
            g_values[neighbor] = tentative_g

    print("Goal not reachable.")

a_star('S', 'G')
