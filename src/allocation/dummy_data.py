import random

# num_orders = 10
# num_workers = 20
# required_stevedores = [2, 4, 4]
#
# worker_preferences_randomized = [[random.uniform(0, 1) for _ in range(num_workers)] for _ in range(num_orders)]
#
# central_allocation_randomized = [[random.randint(0, 1) for _ in range(num_workers)] for _ in range(num_orders)]

num_orders = 3
num_workers = 4
required_stevedores = [2, 1]

worker_preferences = [[0.96, 0.70, 0.51, 0.36], [0.25, 0.48, 0.66, 0.80], [0.60, 0.37, 0.55, 0.92]]
central_allocation = [[1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]

