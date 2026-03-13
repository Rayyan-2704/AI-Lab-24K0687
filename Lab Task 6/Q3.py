import random

POPULATION_SIZE = 6
GENERATIONS = 15
MUTATION_RATE = 0.1

def fitness(x):
    return x**2 + 2*x


def binary_to_decimal(binary):
    return int(binary, 2)


def create_chromosome():
    return format(random.randint(0, 31), '05b')


def initialize_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]


def selection(population):
    population = sorted(
        population,
        key=lambda c: fitness(binary_to_decimal(c)),
        reverse=True
    )
    return population[0], population[1]


def crossover(parent1, parent2):
    point = random.randint(1, 4)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def mutation(chromosome):
    if random.random() < MUTATION_RATE:
        pos = random.randint(0, 4)
        chrom_list = list(chromosome)
        chrom_list[pos] = '1' if chrom_list[pos] == '0' else '0'
        chromosome = "".join(chrom_list)

    return chromosome


def genetic_algorithm():
    population = initialize_population()

    for gen in range(GENERATIONS):
        parent1, parent2 = selection(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        population[-1] = child1
        population[-2] = child2

    best = max(population, key=lambda c: fitness(binary_to_decimal(c)))
    return best


def main():
    best_chromosome = genetic_algorithm()
    best_x = binary_to_decimal(best_chromosome)

    print(f"Best Chromosome: {best_chromosome}")
    print(f"Best value of x: {best_x}")
    print(f"Best Fitness: {fitness(best_x)}")


main()