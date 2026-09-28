import random
items = [5, 7, 8, 2, 4, 6, 3]  
bin_capacity = 10  
population_size = 10  
generations = 100  
mutation_rate = 0.1  
def create_packing():
    bins = []
    for item in items:
        placed = False
        for b in bins:  
            if sum(b) + item <= bin_capacity:
                b.append(item)
                placed = True
                break
        if not placed:  
            bins.append([item])
    return bins 
def create_population():
    return [create_packing() for _ in range(population_size)]
def fitness(solution):
    return len(solution)
def select_best(population):
    return sorted(population, key=fitness)[:population_size // 2]
def crossover(parent1, parent2):
    split = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split] + parent2[split:]  
    child2 = parent2[:split] + parent1[split:]
    return child1, child2
def mutate(solution):
    if random.random() < mutation_rate:
        if len(solution) > 1:  
            i, j = random.sample(range(len(solution)), 2)  
            if solution[i] and solution[j]:  
                item = solution[i].pop(random.randint(0, len(solution[i]) - 1))
                if sum(solution[j]) + item <= bin_capacity:  
                    solution[j].append(item)
                else:
                    solution[i].append(item)  
def run_algorithm():
    population = create_population()  
    for _ in range(generations):
        best_solutions = select_best(population)  
        new_solutions = []
        while len(new_solutions) < population_size:
            parent1, parent2 = random.sample(best_solutions, 2)
            child1, child2 = crossover(parent1, parent2) 
            mutate(child1)
            mutate(child2)
            new_solutions.extend([child1, child2])  
        population = new_solutions[:population_size]  
    best_solution = min(population, key=fitness)
    return best_solution, fitness(best_solution)
best_packing, best_bin_count = run_algorithm()
print("Best Packing Arrangement:", best_packing)
print("Minimum Number of Bins Used:", best_bin_count)
