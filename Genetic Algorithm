import random
C, W, V, P, G, M = 50, [10, 20, 30, 40, 50], [60, 100, 120, 150, 200], 50, 100, 0.1
pop = [[random.randint(0, 1) for _ in W] for _ in range(P)]
def fitness(ch):
    w, v = sum(c * x for c, x in zip(ch, W)), sum(c * x for c, x in zip(ch, V))
    return v if w <= C else 0
for _ in range(G):
    pop = sorted(pop, key=fitness, reverse=True)[:P//2]  
    pop = [random.choice(pop)[:] for _ in range(P)]
    for i in range(0, P, 2):  
        cp = random.randint(1, len(W) - 1)
        pop[i], pop[i+1] = pop[i][:cp] + pop[i+1][cp:], pop[i+1][:cp] + pop[i][cp:]
    for ch in pop:  
        if random.random() < M: ch[random.randint(0, len(W) - 1)] ^= 1
best = max(pop, key=fitness)
print("Best Solution:", best, "Max Value:", fitness(best))
