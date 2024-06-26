from genetic_algorithm import initialization, calc_score, selection, crossover, elitistUpdate, mutation, find_best_chromosome
import read_data
import random
import matplotlib.pyplot as plt
import time
import dummy_data
# Record the start time
start_time = time.time()


# Access the data from read_data.py ( Uncomment if you want to read your own data from read_data.py file )
# worker_preferences = read_data.worker_pref_data
# central_allocation = read_data.filtered_central_allocations

# Access dummy data from dummy_data.py
worker_preferences = dummy_data.worker_preferences
central_allocation = dummy_data.central_allocation

# Weight for central allocation and worker preference scores
weight_central = 0.6
weight_worker = 0.4

required_stevedores = dummy_data.required_stevedores

num_machines = sum(required_stevedores)

# Number of population
Npop = 200

# Number of machines (chromosomes)
n = num_machines
# Probability of crossover
Pc = 0.5
# Probability of mutation (!! use lower mutation probability for better results)
Pm = 0.2
# Stopping number for generation
stopGeneration = 50

# Number of Workers
nu_workers = 20

# Initialize the population
population = initialization(Npop, n, nu_workers)

gen_stats = []  # Initialize empty list for generation statistics

for i in range(stopGeneration):
    # Selecting parents
    parents = selection(population, central_allocation, worker_preferences, weight_central, weight_worker)
    childs = []

    # Apply crossover
    for p in parents:
        r = random.random()
        n = len(population[p[0]])

        if r < Pc:
            childs.append(crossover([population[p[0]], population[p[1]]], n))
        else:
            if r < 0.5:
                childs.append(population[p[0]])
            else:
                childs.append(population[p[1]])

    # Apply mutation
    for c in childs:
        r = random.random()
        if r < Pm:
            c = mutation(c)

    # Update the population
    population = elitistUpdate(population, childs, central_allocation, worker_preferences, weight_central, weight_worker)
    # Calculate scores for each chromosome in the population
    scores = [calc_score(chromosome, central_allocation, worker_preferences, weight_central, weight_worker) for chromosome in population]
    avg_score = sum(scores) / len(scores)

    # Append generation statistics to list
    gen_stats.append({
        'average_score': avg_score,
        'best_score': max(scores)
    })


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

#Find the best solution and best score
best_solution, best_score = find_best_chromosome(population, central_allocation, worker_preferences, weight_central, weight_worker)
print(f"Best solution:{best_solution}")
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

best_solution_type = type(best_solution)
print(f"Type of best_solution: {best_solution_type}")

# Print the elapsed time
print(f"Execution time: {elapsed_time} seconds")

 # Generate the plot
num_generations = stopGeneration
# Define the x and y data for the plot
x_data = range(num_generations)
avg_scores = [stats['average_score'] for stats in gen_stats]
best_scores = [stats['best_score'] for stats in gen_stats]

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the two lines with different colors and labels
ax.plot(x_data, avg_scores, label='Average Score')
ax.plot(x_data, best_scores, label='Best Score')

# Set the axis labels and title
ax.set_xlabel('Generation')
ax.set_ylabel('Score')
ax.set_title('Evolution of Scores over Generations')

# Show the legend
ax.legend()

# Display the plot
plt.show()

