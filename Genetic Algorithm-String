import random, string
TARGET = "Harshitha"
POP_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 30
def random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in TARGET)
def fitness(ind):
    return sum(a == b for a, b in zip(ind, TARGET))
def mutate(ind):
    return ''.join(c if random.random() > MUTATION_RATE else random.choice(string.ascii_letters) for c in ind)
def crossover(p1, p2):
    point = random.randint(1, len(TARGET) - 1)
    return p1[:point] + p2[point:]
def genetic_algorithm():
    population = [random_string() for _ in range(POP_SIZE)]   
    for gen in range(1, GENERATIONS + 1):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print(f"Gen: {gen}  String: {best}  Fitness: {fitness(best)}")
        if best == TARGET:
            print(f"Target '{TARGET}' reached in {gen} generations!")
            break
        parents = population[:POP_SIZE // 2]
        population = [mutate(crossover(random.choice(parents), random.choice(parents))) for _ in range(POP_SIZE)]
genetic_algorithm()
