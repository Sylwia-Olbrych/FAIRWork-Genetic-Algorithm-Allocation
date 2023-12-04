import pytest
from allocation.genetic_algorithm import (
    initialization,
    calc_score,
    selection,
    crossover,
    elitistUpdate,
    mutation,
    find_best_chromosome,
)

from allocation.dummy_data import num_orders, num_workers, required_stevedores, worker_preferences, central_allocation


def test_initialization():
    # Test the initialization function
    Npop = 10
    n = 5
    n_workers = 5
    population = initialization(Npop, n, n_workers)

    # Perform assertions based on your expectations
    assert len(population) == Npop

    for chromosome in population:
        assert len(chromosome) == n
        assert all(0 <= gene < n_workers for gene in chromosome)


def test_calc_score():
    # Test the calc_score function
    chromosome = [1, 2, 0]
    data1 = [[0.96, 0.70, 0.51, 0.36], [0.25, 0.48, 0.66, 0.80], [0.60, 0.37, 0.55, 0.92]]
    data2 = [[1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]

    weight1 = 0.6
    weight2 = 0.4
    score = calc_score(chromosome, data1, data2, weight1, weight2)

    # Perform assertions based on your expectations
    assert isinstance(score, (int, float))
def test_calc_score():
    # Test the calc_score function
    chromosome = [1, 2, 0, 1]
    data1 = [[0.5, 0.8, 0.2], [0.4, 0.6, 0.1], [0.7, 0.9, 0.3], [0.3, 0.5, 0.8]]
    data2 = [[0.2, 0.5, 0.7], [0.1, 0.3, 0.6], [0.8, 0.2, 0.4], [0.5, 0.7, 0.9]]
    weight1 = 0.6
    weight2 = 0.4
    score = calc_score(chromosome, data1, data2, weight1, weight2)

    # Perform assertions based on your expectations
    assert isinstance(score, (int, float))
def test_crossover():
    # Test the crossover function
    parents = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    n = 5
    child = crossover(parents, n)

    # Perform assertions based on your expectations
    assert len(child) == n
    assert set(child) == set(parents[0] + parents[1])
    assert set(child) == set(range(1, n + 1))



def test_mutation():
    # Test the mutation function
    chromosome = [1, 2, 3, 4, 5]
    mutated_chromosome = mutation(chromosome)

    # Perform assertions based on your expectations
    assert len(mutated_chromosome) == len(chromosome)
    assert set(mutated_chromosome) == set(chromosome)

def test_find_best_chromosome():
    # Test the find_best_chromosome function
    population = [[1, 2, 0], [3, 2, 1], [2, 3, 1]]
    data1 = [[0.96, 0.70, 0.51, 0.36], [0.25, 0.48, 0.66, 0.80], [0.60, 0.37, 0.55, 0.92]]
    data2 = [[1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]

    weight1 = 0.6
    weight2 = 0.4
    best_chromosome, best_score = find_best_chromosome(population, data1, data2, weight1, weight2)

    # Perform assertions based on your expectations
    assert len(best_chromosome) == len(population[0])
    assert isinstance(best_score, (int, float))

def test_dummy_data_types():
    # Check the types of num_orders, num_workers, and required_stevedores
    assert isinstance(num_orders, int)
    assert isinstance(num_workers, int)
    assert isinstance(required_stevedores, list)
    assert all(isinstance(val, int) for val in required_stevedores)

    # Check the type and shape of worker_preferences
    assert isinstance(worker_preferences, list)
    assert all(isinstance(row, list) for row in worker_preferences)
    assert all(isinstance(val, (int, float)) for row in worker_preferences for val in row)
    assert all(len(row) == num_workers for row in worker_preferences)
    assert len(worker_preferences) == num_orders

    # Check the type and shape of central_allocation
    assert isinstance(central_allocation, list)
    assert all(isinstance(row, list) for row in central_allocation)
    assert all(isinstance(val, int) for row in central_allocation for val in row)
    assert all(len(row) == num_workers for row in central_allocation)
    assert len(central_allocation) == num_orders


if __name__ == '__main__':
    pytest.main()