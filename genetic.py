import random 

def fitness_function(chromosome):
    x = int("".join(map(str, chromosome)), 2)
    return x ** 2

population_size = int(input("Enter the population size: "))
chromosome_length = int(input("Enter the chromosome length: "))
generations = int(input("Enter the number of generations: "))
mutation_rate = float(input("Enter the mutation rate (%): ")) / 100

population = []
for _ in range(population_size):
    chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
    population.append(chromosome)

for _ in range(generations):
    fitness_scores = []
    for chromosome in population:
        fitness = fitness_function(chromosome)
        fitness_scores.append(fitness)

    parents = []
    for _ in range(population_size):
        parents.append(random.choice(population))

    children = []
    for i in range(0, len(parents), 2):
        crossover_point = random.randint(0, chromosome_length-1)
        parent1 = parents[i]
        parent2 = parents[i+1]

        child1 = parent1[:crossover_point] + parent2[crossover_point:] 
        child2 = parent2[:crossover_point] + parent1[crossover_point:] 
    
        for j in range(chromosome_length):
            if random.random() < mutation_rate:
                child1[j] ^= 1
            if random.random() < mutation_rate:
                child2[j] ^= 1

        children.append(child1)
        children.append(child2)

    population = children

best_chromosome = max(population, key=lambda a: fitness_function(a))
best_fitness = fitness_function(best_chromosome)
best_x = best_fitness ** 0.5

print("Best Chromosome:", best_chromosome)
print("Best Fitness:", best_fitness)
print("Corresponding X Value:", best_x)
