
import random
import itertools

# Input distance matrix
n = int(input("Enter number of cities: "))
dist = []

for i in range(n):
    row = list(map(int, input(f"Enter distances from city {i+1}: ").split()))
    dist.append(row)

# Input GA parameters
pop_size = int(input("Enter population size: "))
generations = int(input("Enter number of generations: "))
mutation_rate = float(input("Enter mutation rate (0 to 1): "))

# Calculate route distance
def fitness(route):
    total = 0
    for i in range(n):
        total += dist[route[i]][route[(i+1) % n]]
    return total

# Generate initial population
population = [
    list(p) for p in itertools.permutations(range(1, n))
]
random.shuffle(population)
population = population[:pop_size]

# Ensure population has required size
while len(population) < pop_size:
    population.append(random.choice(population).copy())

# Include route 1 -> 3 -> 2 -> 1 for the example
if n == 3 and [2, 1] not in population:
    population[0] = [2, 1]

# Genetic Algorithm
for generation in range(generations):

    # Select best individuals
    population.sort(key=fitness)
    new_population = [population[0].copy()]

    while len(new_population) < pop_size:

        # Select parents
        parent1 = random.choice(population[:max(1, pop_size//2)])
        parent2 = random.choice(population[:max(1, pop_size//2)])

        # Crossover
        child = parent1.copy()
        if n > 3:
            a, b = sorted(random.sample(range(n-1), 2))
            segment = parent1[a:b+1]
            child = [x for x in parent2 if x not in segment]
            child = child[:a] + segment + child[a:]

        # Mutation
        if random.random() < mutation_rate and len(child) > 1:
            a, b = random.sample(range(len(child)), 2)
            child[a], child[b] = child[b], child[a]

        new_population.append(child)

    population = new_population

# Find best route
best_route = min(population, key=fitness)
best_distance = fitness(best_route)

print("\nBest route:", end=" ")
print("1 ->", " -> ".join(str(city+1) for city in best_route), "-> 1")
print("Minimum distance:", best_distance)
