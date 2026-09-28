import math
game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}
minimax_cache = {}
def minimax(node, is_max):
    if node in minimax_cache:
        return minimax_cache[node]
    if isinstance(game_tree[node], int):
        minimax_cache[node] = game_tree[node] 
        return game_tree[node]
    children = game_tree[node]
    values = [minimax(child, not is_max) for child in children]
    best_value = max(values) if is_max else min(values)
    minimax_cache[node] = best_value  
    return best_value
def find_optimal_path(node, is_max):
    path = [node]
    while node in game_tree and not isinstance(game_tree[node], int):  # Stop at leaf node
        children = game_tree[node]
        next_node = max(children, key=lambda c: minimax_cache.get(c, game_tree[c])) if is_max else min(children, key=lambda c: minimax_cache.get(c, game_tree[c]))
        path.append(next_node)
        node = next_node
        is_max = not is_max  
    return path
optimal_value = minimax('A', True)
optimal_path = find_optimal_path('A', True)
print(f"\033[1;32mOptimal Value:\033[0m {optimal_value}")
print(f"\033[1;34mOptimal Path:\033[0m {' -> '.join(optimal_path)}")
