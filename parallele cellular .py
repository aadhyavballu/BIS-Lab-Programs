
import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor

# 1. Define the objective function
def objective(x):
    return x ** 2


# 2. Initialize parameters
ROWS = 10
COLS = 10
GENERATIONS = 100
MUTATION_RATE = 0.1
MIN_VALUE = -10
MAX_VALUE = 10

# 3. Initialize population
random.seed(42)
np.random.seed(42)

population = np.random.uniform(
    MIN_VALUE, MAX_VALUE, (ROWS, COLS)
)

# 4. Evaluate fitness
fitness = np.vectorize(objective)(population)


# Find neighbouring cells
def get_neighbors(i, j, pop):
    neighbors = []

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni = (i + di) % ROWS
            nj = (j + dj) % COLS
            neighbors.append(pop[ni, nj])

    return neighbors


# 5. Update each cell
def update_cell(args):
    i, j, pop, generation = args

    rng = random.Random(42 + generation * 1000 + i * COLS + j)

    neighbors = get_neighbors(i, j, pop)

    # Select two parents based on fitness
    parents = sorted(neighbors, key=objective)

    parent1 = parents[0]
    parent2 = parents[rng.randrange(len(parents))]

    # 6. Crossover
    alpha = rng.random()
    child = alpha * parent1 + (1 - alpha) * parent2

    # 7. Mutation
    if rng.random() < MUTATION_RATE:
        child += rng.gauss(0, 0.5)

    # 8. Boundary checking
    child = np.clip(child, MIN_VALUE, MAX_VALUE)

    # Elitism: retain the better solution
    if objective(child) < objective(pop[i, j]):
        return child

    return pop[i, j]


# 9. Run parallel cellular genetic algorithm
with ThreadPoolExecutor() as executor:

    for generation in range(1, GENERATIONS + 1):

        tasks = [
            (i, j, population.copy(), generation)
            for i in range(ROWS)
            for j in range(COLS)
        ]

        new_values = list(executor.map(update_cell, tasks))

        population = np.array(new_values).reshape(ROWS, COLS)

        # Local refinement of the best solution
        best_index = np.unravel_index(
            np.argmin(population ** 2), population.shape
        )

        best_x = population[best_index]

        refined_x = best_x * random.random()

        if objective(refined_x) < objective(best_x):
            population[best_index] = refined_x

        # Evaluate fitness
        fitness = np.vectorize(objective)(population)

        # Find best fitness
        best_fitness = np.min(fitness)

        print(
            f"Generation : {generation} "
            f"Best Fitness : {best_fitness:.6f}"
        )


# 10. Display final result
best_index = np.unravel_index(
    np.argmin(fitness), fitness.shape
)

best_solution = population[best_index]

print("\nOPTIMAL SOLUTION")
print("Best Position:", best_solution)
print("Minimum Fitness:", objective(best_solution))
