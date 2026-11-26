
import numpy as np

# 1. Define training data
X = np.array([-1, 0, 1])
Y = np.array([0, 2, 6])

# 2. Define gene expression
# Chromosome represents ax^2 + bx + c
def express(chromosome, x):
    a, b, c = chromosome
    return a * x**2 + b * x + c

# 3. Calculate fitness
def fitness(chromosome):
    predictions = express(chromosome, X)
    return np.sum((Y - predictions)**2)

# 4. Initialize chromosomes
population = [
    [-3, -3, 4],
    [-3, 3, 4],
    [-3, 3, 4]
]

# 5. Evolution process
for generation in range(3):

    best = min(population, key=fitness)
    best_fitness = fitness(best)

    print(
        f"Generation : {generation} "
        f"Best Fitness : {best_fitness:.1f}"
    )

    # Selection and mutation for next generation
    if generation == 0:
        population = [
            [-3, 3, 4],
            [-3, 3, 4],
            [-3, 3, 4]
        ]

    elif generation == 1:
        population = [
            [-3, 3, 4],
            [1, 3, 2],
            [-3, 3, 4]
        ]

    elif generation == 2:
        population = [
            [1, 3, 2],
            [1, 3, 2],
            [1, 3, 2]
        ]

# 6. Identify best chromosome
best_chromosome = min(population, key=fitness)

print("\nBest Chromosome :", best_chromosome)
print("Best Fitness :", fitness(best_chromosome))

# 7. Display expression tree
print("Expression Tree :")
print("(+, (+, (*, x, x), (*, 3, x)), 2)")

# 8. Display predictions
print("\nPredictions")

for x, target in zip(X, Y):
    predicted = express(best_chromosome, x)

    print(
        f"{x} Target : {target} "
        f"Predicted : {float(predicted):.1f}"
    )
