import numpy as np
from random import random, shuffle, randint


def single_cell_crossover(parent1, parent2, cross_probability: float):
    child = np.empty((9, 9), dtype=np.int8)
    for row in range(9):
        for col in range(9):
            random_number = random()
            if random_number <= cross_probability:
                child[row, col] = parent1[row, col].copy()
            elif random_number <= (2.0 * cross_probability):
                child[row, col] = parent2[row, col].copy()
            else:
                child[row, col] = randint(1, 9)
    return child


def row_crossover(parent1, parent2, cross_probability: float):
    child = np.empty((9, 9), dtype=np.int8)
    for row in range(9):
        random_number = random()
        if random_number <= cross_probability:
            child[row, :] = parent1[row, :].copy()
        elif random_number <= (2.0 * cross_probability):
            child[row, :] = parent2[row, :].copy()
        else:
            sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            shuffle(sample)
            child[row, :] = sample
    return child
