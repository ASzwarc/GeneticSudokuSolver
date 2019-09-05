import numpy as np
from random import shuffle
from collections import namedtuple
# TODO Maybe move algorithm parameters to separate config file
POPULATION_SIZE = 20
GENERATION_COUNT = 20
SHUFFLE_NO = 3

# Genetic algorithm:
# 1. generate initial population
# 2. compute fitness
# 3. LOOP: selection, crossover, mutation, compute fitness

Item = namedtuple("Item", ["row", "col", "value"])


class Generation():
    def __init__(self, size, board):
        self._population = [self.generate_sample() for _ in range(size)]
        self._board = board

    def generate_sample(self):
        def shuffle_sample():
            sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for _ in range(SHUFFLE_NO):
                shuffle(sample)
            return sample

        return np.array([shuffle_sample() for _ in range(9)], dtype=np.int8)

    def compute_fitness(self, sample_no):
        def calc_column_penalty(column_sum):
            return 45 - column_sum

        # calculate sum of each square, penaly is 45 - sum
        incorrect_fixed_value_penalty = -10
        fitness = 0
        # incorrect sum in column
        v_calc_column_penalty = np.vectorize(calc_column_penalty)
        fitness = np.sum(v_calc_column_penalty(np.sum(
                    self._population[sample_no],
                    axis=0)))
        # incorrect sum in square
        flat_sample = self._population[sample_no].flatten()
        for idx in range(0, 27, 3):

        # incorrect known item
        for item in self._board.items:
            if self._population[sample_no][item.row, item.col] != item.value:
                fitness += incorrect_fixed_value_penalty

        return fitness


class Board():
    def __init__(self):
        self._items = self.inject_board()

    @property
    def items(self):
        return self._items

    def inject_board(self):
        """
        Helper function for injecting solvable sudoku board.
        Board taken from this page, section "Easiest":
        https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
        """

        board = []
        board.append(Item._make([0, 3, 2]))
        board.append(Item._make([0, 4, 6]))
        board.append(Item._make([0, 6, 7]))
        board.append(Item._make([0, 8, 1]))

        board.append(Item._make([1, 0, 6]))
        board.append(Item._make([1, 1, 8]))
        board.append(Item._make([1, 4, 7]))
        board.append(Item._make([1, 7, 9]))

        board.append(Item._make([2, 0, 1]))
        board.append(Item._make([2, 1, 9]))
        board.append(Item._make([2, 5, 4]))
        board.append(Item._make([2, 6, 5]))

        board.append(Item._make([3, 0, 8]))
        board.append(Item._make([3, 1, 2]))
        board.append(Item._make([3, 3, 1]))
        board.append(Item._make([3, 7, 4]))

        board.append(Item._make([4, 2, 4]))
        board.append(Item._make([4, 3, 6]))
        board.append(Item._make([4, 5, 2]))
        board.append(Item._make([4, 6, 9]))

        board.append(Item._make([5, 1, 5]))
        board.append(Item._make([5, 5, 3]))
        board.append(Item._make([5, 7, 2]))
        board.append(Item._make([5, 8, 8]))

        board.append(Item._make([6, 2, 9]))
        board.append(Item._make([6, 3, 3]))
        board.append(Item._make([6, 7, 7]))
        board.append(Item._make([6, 8, 4]))

        board.append(Item._make([7, 1, 4]))
        board.append(Item._make([7, 4, 5]))
        board.append(Item._make([7, 7, 3]))
        board.append(Item._make([7, 8, 6]))

        board.append(Item._make([8, 0, 7]))
        board.append(Item._make([8, 2, 3]))
        board.append(Item._make([8, 4, 1]))
        board.append(Item._make([8, 5, 8]))

        return board

if __name__ == "__main__":
    board = Board()
    print(board._items)
    population = Generation(POPULATION_SIZE)
    for no in range(POPULATION_SIZE):
        print(f"Sample #{no}")
        print(population._population[no])
        print("-------------------------------------")
