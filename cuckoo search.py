
import random
import math

# Objective function
def fitness(x):
    return sum(i * i for i in x)

# Levy flight using Mantegna's algorithm
def levy_flight():
    beta = 1.5
    sigma = (
        math.gamma(1 + beta) * math.sin(math.pi * beta / 2) /
        (math.gamma((1 + beta) / 2) * beta *
         2 ** ((beta - 1) / 2))
    ) ** (1 / beta)

    u = random.gauss(0, sigma)
    v = random.gauss(0, 1)

    return u / (abs(v) ** (1 / beta))

# Input parameters
n = int(input("Enter number of nests: "))
dim = int(input("Enter number of dimensions: "))
iterations = int(input("Enter number of iterations: "))

# Algorithm parameters
pa = 0.25
alpha = 0.1
lower = -5
upper = 5

# Initialize nests randomly
nests = [
    [random.uniform(lower, upper) for j in range(dim)]
    for i in range(n)
]

# Find initial best solution
best_nest = min(nests, key=fitness).copy()
best_fitness = fitness(best_nest)

# Cuckoo Search Algorithm
for iteration in range(1, iterations + 1):

    # Generate new solutions using Levy flight
    for i in range(n):

        new_nest = [
            nests[i][j] + alpha * levy_flight()
            for j in range(dim)
        ]

        # Apply boundary limits
        new_nest = [
            max(lower, min(upper, x))
            for x in new_nest
        ]

        # Select a random nest
        k = random.randint(0, n - 1)

        # Replace nest if new solution is better
        if fitness(new_nest) < fitness(nests[k]):
            nests[k] = new_nest

    # Abandon worst nests and generate new solutions
    for i in range(n):
        if random.random() < pa:
            nests[i] = [
                random.uniform(lower, upper)
                for j in range(dim)
            ]

    # Update global best solution
    current_best = min(nests, key=fitness)

    if fitness(current_best) < best_fitness:
        best_nest = current_best.copy()
        best_fitness = fitness(best_nest)

    # Display iteration result
    print("Iteration", iteration,
          ": Best fitness =", round(best_fitness, 6))

# Final result
print("\nFinal Result")
print("Best Position:", best_nest)
print("Minimum Fitness:", best_fitness)

print("\nApplications:")
print("Engineering design optimization")
print("Feature selection in machine learning")
print("Scheduling and resource allocation")

print("\nReference:")
print("X. S. Yang and S. Deb,")
print("Cuckoo Search via Levy Flights, 2009.")
