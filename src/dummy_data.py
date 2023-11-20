import random

num_orders = 10
num_workers = 20

worker_preferences_randomized = [[random.uniform(0, 1) for _ in range(num_workers)] for _ in range(num_orders)]

central_allocation_randomized = [[random.randint(0, 1) for _ in range(num_workers)] for _ in range(num_orders)]

