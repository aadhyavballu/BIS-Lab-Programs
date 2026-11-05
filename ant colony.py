
import random

# Input number of cities
n = int(input("Enter the number of cities: "))

# Input distance matrix
dist = []
for i in range(n):
    row = list(map(int, input(f"Enter distances from city {i}: ").split()))
    dist.append(row)

# Input parameters
ants = int(input("Enter number of ants: "))
iterations = int(input("Enter number of iterations: "))

# ACO parameters
alpha = 1
beta = 2
evaporation = 0.5
Q = 100

# Initialize pheromone levels
pheromone = [[1.0 for j in range(n)] for i in range(n)]

best_route = None
best_distance = float('inf')

# Ant Colony Optimization
for iteration in range(iterations):

    for ant in range(ants):

        # Select random starting city
        start = random.randint(0, n-1)
        route = [start]
        unvisited = list(range(n))
        unvisited.remove(start)

        # Construct route
        while unvisited:
            current = route[-1]

            probabilities = []
            for city in unvisited:
                p = (pheromone[current][city] ** alpha) * \
                    ((1 / dist[current][city]) ** beta)
                probabilities.append(p)

            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]

            next_city = random.choices(
                unvisited, weights=probabilities, k=1
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        # Return to starting city
        route.append(start)

        # Calculate total distance
        distance = sum(
            dist[route[i]][route[i+1]]
            for i in range(n)
        )

        # Update best route
        if distance < best_distance:
            best_distance = distance
            best_route = route.copy()

        # Update pheromone
        for i in range(n):
            a = route[i]
            b = route[i+1]
            pheromone[a][b] += Q / distance
            pheromone[b][a] += Q / distance

    # Pheromone evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)

# Final output
print("\nOutput:")
print("Enter the number of ants:", ants)
print("Enter number of iterations:", iterations)
print("Best Route:", best_route)
print("Shortest Distance:", best_distance)

print("\nApplications:")
print("Shortest path and route optimization")
print("Delivery and transportation")
print("Job scheduling")
print("Computer network routing")

print("\nReference:")
print("Ant Colony Optimization by Marco Dorigo, 1992.")
