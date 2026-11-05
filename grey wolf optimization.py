
import random

# Objective function
def fitness(x):
    return sum(i * i for i in x)

# Input
n = int(input("Enter number of wolves: "))
dim = int(input("Enter number of dimensions: "))
iterations = int(input("Enter number of iterations: "))

# Initialize wolves
wolves = [
    [random.uniform(-10, 10) for j in range(dim)]
    for i in range(n)
]

# Grey Wolf Optimization
for t in range(iterations):

    # Sort wolves based on fitness
    wolves.sort(key=fitness)

    alpha = wolves[0].copy()
    beta = wolves[1].copy()
    delta = wolves[2].copy()

    # Decreasing parameter
    a = 2 - 2 * t / iterations

    # Update wolf positions
    for i in range(3, n):
        for j in range(dim):

            r1, r2 = random.random(), random.random()
            A1 = 2 * a * r1 - a
            C1 = 2 * r2
            D_alpha = abs(C1 * alpha[j] - wolves[i][j])
            X1 = alpha[j] - A1 * D_alpha

            r1, r2 = random.random(), random.random()
            A2 = 2 * a * r1 - a
            C2 = 2 * r2
            D_beta = abs(C2 * beta[j] - wolves[i][j])
            X2 = beta[j] - A2 * D_beta

            r1, r2 = random.random(), random.random()
            A3 = 2 * a * r1 - a
            C3 = 2 * r2
            D_delta = abs(C3 * delta[j] - wolves[i][j])
            X3 = delta[j] - A3 * D_delta

            wolves[i][j] = (X1 + X2 + X3) / 3

    # Keep the best three wolves unchanged
    wolves[0] = alpha
    wolves[1] = beta
    wolves[2] = delta

    # Find best solution
    wolves.sort(key=fitness)
    best_position = wolves[0].copy()
    best_value = fitness(best_position)

    print("Iteration", t + 1,
          ": Best fitness =", round(best_value, 6))

# Final result
print("\nFinal Result")
print("Best Position:", best_position)
print("Minimum Fitness:", best_value)

print("\nApplications:")
print("Engineering design optimization")
print("Feature selection in machine learning")
print("Scheduling and resource allocation")

print("\nReference:")
print("S. Mirjalili, S. M. Mirjalili and A. Lewis, 2014")
print("Grey Wolf Optimizer, Advances in Engineering Software")
