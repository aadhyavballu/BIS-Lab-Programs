
import random

# Objective function
def fitness(x):
    return x ** 2

# Input parameters
n = int(input("Enter number of particles: "))
iterations = int(input("Enter number of iterations: "))

# PSO parameters
w = 0.5
c1 = 1.5
c2 = 1.5

# Initialize particles
position = [random.uniform(-10, 10) for i in range(n)]
velocity = [random.uniform(-1, 1) for i in range(n)]

pbest = position.copy()
pbest_value = [fitness(x) for x in position]

gbest_index = pbest_value.index(min(pbest_value))
gbest = pbest[gbest_index]
gbest_value = pbest_value[gbest_index]

# PSO iterations
for iteration in range(1, iterations + 1):

    for i in range(n):

        r1 = random.random()
        r2 = random.random()

        velocity[i] = (
            w * velocity[i]
            + c1 * r1 * (pbest[i] - position[i])
            + c2 * r2 * (gbest - position[i])
        )

        position[i] += velocity[i]

        value = fitness(position[i])

        if value < pbest_value[i]:
            pbest[i] = position[i]
            pbest_value[i] = value

        if value < gbest_value:
            gbest = position[i]
            gbest_value = value

    print("\nIteration:", iteration)
    print("Best Position:", round(gbest, 10))
    print("Best Value:", round(gbest_value, 10))

# Final result
print("\nFinal Result")
print("Best Position:", gbest)
print("Minimum Value:", gbest_value)

print("\nApplications:")
print("Machine learning and neural networks")
print("Engineering design")
print("Resource allocation")

print("\nReference:")
print("Particle Swarm Optimization by J. Kennedy and R. Eberhart, 1995.")
