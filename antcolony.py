import random

# Number of cities
N = int(input("Enter the number of cities: "))

# Input distances matrix
print("Enter the distances between cities:")
distances = []
for i in range(N):
    row = list(map(int, input().split()))
    distances.append(row)

# Initialize pheromones as an all-ones matrix
pheromones = [[1] * N for _ in range(N)]

def select_next_city(visited, curr_city):
    pheromone_value = [pheromones[curr_city][j] if not visited[j] else 0 for j in range(N)]
    heuristic_info = [1 / (distances[curr_city][j] + 1e-10) for j in range(N)]
    probabilities = [pheromone_value[j] * (heuristic_info[j]**2) for j in range(N)]
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]
    next_city = random.choices(range(N), probabilities)[0]
    return next_city

def ant_tour():
    visited = [False] * N
    tour = [0]
    curr_city = 0
    total_dist = 0

    while(len(tour) < N):
        next_city = select_next_city(visited, curr_city)
        tour.append(next_city)
        visited[next_city] = True
        total_dist += distances[curr_city][next_city]
        curr_city = next_city

    total_dist += distances[curr_city][0]
    return tour, total_dist

best_tour, total_dist = ant_tour()
print("Best Tour:", best_tour)
print("Total Distance:", total_dist)
