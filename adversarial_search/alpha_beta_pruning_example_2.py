import math
def alpha_beta_cutoff(node, depth, alpha, beta, maximize):
    if isinstance(game_tree[node], int):  
        return game_tree[node]
    if maximize:
        best_value = -math.inf
        for child in game_tree[node]:
            value = alpha_beta_cutoff(child, depth + 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break  
        return best_value
    else:
        best_value = math.inf
        for child in game_tree[node]:
            value = alpha_beta_cutoff(child, depth + 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break 
        return best_value
def get_optimal_sequence(node, alpha, beta, maximize):
    sequence = [node]
    while node in game_tree and not isinstance(game_tree[node], int):
        if maximize:
            best_value = -math.inf
            best_child = None
            for child in game_tree[node]:
                value = alpha_beta_cutoff(child, 0, alpha, beta, False)
                if value > best_value:
                    best_value = value
                    best_child = child
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
        else:
            best_value = math.inf
            best_child = None
            for child in game_tree[node]:
                value = alpha_beta_cutoff(child, 0, alpha, beta, True)
                if value < best_value:
                    best_value = value
                    best_child = child
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
        sequence.append(best_child)
        node = best_child
        maximize = not maximize  
    return sequence
game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}
optimal_value = alpha_beta_cutoff('A', 0, -math.inf, math.inf, True)
optimal_sequence = get_optimal_sequence('A', -math.inf, math.inf, True)
print("Optimal Value:", optimal_value)
print("Optimal Sequence:", " -> ".join(optimal_sequence))
