import numpy as np
import random

def initialization(Npop, n, n_workers):
    # List of workers from worker 0 to worker 19 (starting with 0)
    workers = list(range(n_workers))

    # Function to create a random chromosome
    def create_chromosome(num_workers):
        return random.sample(workers, num_workers)

    # Initialize the population
    population = [create_chromosome(n) for _ in range(Npop)]

    return population


def calc_score(chromosome, data1, data2, weight1, weight2):
    #data1 : machine pref/central allocation
    #data2 : worker preference
    data1 = np.array(data1)
    data2 = np.array(data2)
    result1 = np.zeros(len(chromosome))
    result2 = np.zeros(len(chromosome))
    for i, idx in enumerate(chromosome):
        if idx < len(data1[i]):
            result1[i] = data1[i][idx]
        if idx < len(data2[i]):
            result2[i] = data2[i][idx]
    sum_output1 = np.sum(result1)
    sum_output2 = np.sum(result2)

    # print(result1)
    # print("Sum of Machine Pref:", sum_output1)  # Sum of output1
    # print(result2)
    # print("Sum of Worker Pref:", sum_output2)  # Sum of output2
    # Print the intermediate results for debugging

    # print("Result1:")
    # print(result1)
    # print("Result2:")
    # print(result2)
    total_score = weight1*sum_output1 + weight2*sum_output2

    return total_score
# # Sample data and weights
# chromosome = [1, 2, 0]  # Sample chromosome
# data1 = [[10, 20, 30], [5, 15, 25], [8, 18, 28]]  # Sample data1 (machine pref/central allocation)
# data2 = [[5, 10, 15], [3, 8, 13], [4, 9, 14]]  # Sample data2 (worker preference)
# weight1 = 2  # Weight for sum_output1
# weight2 = 1  # Weight for sum_output2
#
# # Call the calc_score function with the sample data and weights
# score = calc_score(chromosome, data2, data1, weight2, weight1)
#
# # Print the result
# print("Total Score:", score)

def selection(pop, machine_pref, worker_pref, weight1, weight2):
    popObj = []
    for i in range(len(pop)):
        popObj.append([calc_score(pop[i], machine_pref, worker_pref, weight1, weight2), i])

    popObj.sort()

    distr = []
    distrInd = []

    for i in range(len(pop)):
        distrInd.append(popObj[i][1])
        prob = (2 * (i + 1)) / (len(pop) * (len(pop) + 1))
        distr.append(prob)

    parents = []
    for i in range(len(pop)):
        # Choose two distinct parents
        parent1 = np.random.choice(distrInd, 1, p=distr)[0]
        parent2 = parent1
        while parent2 == parent1:
            parent2 = np.random.choice(distrInd, 1, p=distr)[0]
        parents.append([parent1, parent2])

    return parents

def crossover(parents, n):
    pos = list(np.random.permutation(np.arange(n - 1) + 1)[:2])

    if pos[0] > pos[1]:
        pos[0], pos[1] = pos[1], pos[0]

    child = [-1] * n

    # Copy over the segment from the first parent
    for i in range(pos[0], pos[1]):
        child[i] = parents[0][i]

    # Fill in the remaining values from the second parent, avoiding repeats
    used_values = set(child)
    j = 0
    for i in range(n):
        if i < pos[0] or i >= pos[1]:
            while parents[1][j] in used_values:
                j += 1
            child[i] = parents[1][j]
            used_values.add(child[i])
            j += 1

    return child

#
# # Test the crossover function
# parent1 = [1, 2, 8]
# parent2 = [5, 4, 3]
# n = len(parent1)
#
# child = crossover([parent1, parent2], n)
#
# print("Parent 1:", parent1)
# print("Parent 2:", parent2)
# print("Child:", child)

def elitistUpdate(old_pop, new_pop, worker_preferences, machine_preferences, weight1, weight2):
    # Calculate fitness scores for all individuals in the population
    old_scores = [calc_score(individual, worker_preferences, machine_preferences, weight1, weight2) for individual in old_pop]
    new_scores = [calc_score(individual, worker_preferences, machine_preferences, weight1, weight2) for individual in new_pop]

    # Find the index of the best individual in the old population
    best_idx = max(range(len(old_scores)), key=lambda i: old_scores[i])

    # Replace the worst individual in the new population with the best individual from the old population
    worst_idx = min(range(len(new_scores)), key=lambda i: new_scores[i])
    new_pop[worst_idx] = old_pop[best_idx]

    return new_pop


# function for mutation
def mutation(chromosome):
    # choose two random positions in the chromosome
    position1, position2 = random.sample(range(len(chromosome)), 2)
    # swap the elements at those positions
    chromosome[position1], chromosome[position2] = chromosome[position2], chromosome[position1]
    return chromosome


def find_best_chromosome(population, machine_pref, worker_pref, weight1, weight2):
    best_chromosome = None
    best_score = float('-inf')

    for chromosome in population:
        score = calc_score(chromosome, machine_pref, worker_pref, weight1, weight2)
        if score > best_score:
            best_chromosome = chromosome
            best_score = score

    return best_chromosome, best_score


