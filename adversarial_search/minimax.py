game_tree = {
    'A': ['B1', 'B2'],
    'B1': ['C1', 'C2'],
    'B2': ['C3', 'C4'],
    'C1': ['D1', 'D2'],
    'C2': ['D3', 'D4'],
    'C3': ['D5', 'D6'],
    'C4': ['D7', 'D8'],
    'D1': ['E1', 'E2'],
    'D2': ['E3', 'E4'],
    'D3': ['E5', 'E6'],
    'D4': ['E7', 'E8'],
    'D5': ['E9', 'E10'],
    'D6': ['E11', 'E12'],
    'D7': ['E13', 'E14'],
    'D8': ['E15', 'E16'],
    'E1': 5, 'E2': -1, 'E3': 4, 'E4': 3,
    'E5': -2, 'E6': -5, 'E7': 9, 'E8': 8,
    'E9': 6, 'E10': 1, 'E11': -4, 'E12': 2,
    'E13': 4, 'E14': 7, 'E15': 3, 'E16': -3
}
def minimax(node, is_max):
    if isinstance(game_tree[node], int):  
        return game_tree[node]    
    children = game_tree[node]
    values = [minimax(child, not is_max) for child in children] 
    return max(values) if is_max else min(values)
def find_optimal_path(node, is_max):
    path = [node]
    while node in game_tree and not isinstance(game_tree[node], int):  # Stop at leaf node
        children = game_tree[node]
        if is_max:
            next_node = max(children, key=lambda c: minimax(c, False))
        else:
            next_node = min(children, key=lambda c: minimax(c, True))       
        path.append(next_node)
        node = next_node
        is_max = not is_max  
    return path
optimal_value = minimax('A', True)
optimal_path = find_optimal_path('A', True)
print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
