from genetic_algorithm import initialization, calc_score, selection, crossover, elitistUpdate, mutation, find_best_chromosome
import read_data
import random
import matplotlib.pyplot as plt
import time
import itertools
# Access the data from read_data.py
worker_preferences = read_data.worker_pref_data
central_allocation = read_data.filtered_central_allocations

weight_central = 0.6
weight_worker = 0.4

# read required number of stevedores from excel sheet
required_stevedores = read_data.n
print(required_stevedores)
num_machines = sum(required_stevedores)

import math

# Define the number of numbers and slots
num_numbers = 20
num_slots = num_machines

# Calculate the total number of permutations
total_permutations = math.perm(num_numbers, num_slots)

print(f"Total number of permutations: {total_permutations}")



# Record the start time
start_time = time.time()




# print(worker_preferences)
# print(resilience_data)
# Number of population
Npop = 116280

# number of orders (chromosomes)
n = num_machines

# Creating the initial population
# 20 workers
# population = initialization(Npop, n, 20)
# print(population)
gen_stats = []  # Initialize empty list for generation statistics
########
import itertools

# Define a set of numbers
# Generate a list of numbers from 0 to 19
numbers = list(range(20))

# Print the list of numbers
print(numbers)



# Generate and print permutations
print("\nPermutations:")
permutations = list(itertools.permutations(numbers, n))
# for permutation in permutations:
#     print(list(permutation))

######
# Create an empty list to store scores for each chromosome
scores = []

with open("population.txt", "w") as file:
    for chromosome in numbers:
        file.write(str(chromosome) + "\n")

# Calculate scores for each chromosome in the population
for chromosome in permutations:
    score = calc_score(chromosome, central_allocation, worker_preferences, weight_central, weight_worker)
    scores.append(score)

# Open a file for writing population data and scores
with open("population_with_scores.txt", "w") as file:
    for i, chromosome in enumerate(permutations):
        # Calculate the score for the current chromosome
        score = calc_score(chromosome, central_allocation, worker_preferences, weight_central, weight_worker)

        # Write both the chromosome and its score to the file
        file.write(f"Chromosome {i}:\n")
        file.write(f"Chromosome Data: {chromosome}\n")
        file.write(f"Score: {score}\n\n")

# Find the best solution and its score
best_score = max(scores)
best_solution = permutations[scores.index(best_score)]

# Print the best solution and its score
print(f"Best solution: {best_solution}")
print(f"Total score: {best_score}")

def print_best_worker_assignments(best_solution, required_stevedores):
    order_start = 0
    for order, num_stevedores in enumerate(required_stevedores, start=1):
        order_workers = best_solution[order_start:order_start + num_stevedores]
        order_start += num_stevedores

        order_str = f"Order {order}"
        # Add 1 to all worker IDs before printing
        order_ids = ", ".join([f"ID {100001 + worker}" for worker in order_workers])
        worker_ids = ", ".join([str(worker) for worker in order_workers])

        print(f"{order_str} - {order_ids} ")


print_best_worker_assignments(best_solution, required_stevedores)


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Execution time: {elapsed_time} seconds")
#########
