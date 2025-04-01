import math
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if isinstance(game_tree[node], int):  
        return game_tree[node]
    if maximizing_player:
        best_value = -math.inf
        for child in game_tree[node]:
            value = alpha_beta_pruning(child, depth + 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:  
                break
        return best_value
    else:
        best_value = math.inf
        for child in game_tree[node]:
            value = alpha_beta_pruning(child, depth + 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:  
                break
        return best_value
def get_best_path(node, alpha, beta, maximizing_player):
    path = [node]
    
    while node in game_tree and not isinstance(game_tree[node], int):
        if maximizing_player:
            best_value = -math.inf
            best_move = None
            for child in game_tree[node]:
                value = alpha_beta_pruning(child, 0, alpha, beta, False)
                if value > best_value:
                    best_value = value
                    best_move = child
                alpha = max(alpha, best_value)
                if beta <= alpha:  
                    break
        else:
            best_value = math.inf
            best_move = None
            for child in game_tree[node]:
                value = alpha_beta_pruning(child, 0, alpha, beta, True)
                if value < best_value:
                    best_value = value
                    best_move = child
                beta = min(beta, best_value)
                if beta <= alpha: 
                    break
        path.append(best_move)
        node = best_move
        maximizing_player = not maximizing_player  
    return path
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
optimal_value = alpha_beta_pruning('A', 0, -math.inf, math.inf, True)
optimal_path = get_best_path('A', -math.inf, math.inf, True)
print("Optimal Value:", optimal_value)
print("Best Path:", " -> ".join(optimal_path))
