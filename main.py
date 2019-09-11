from __future__ import annotations
import numpy as np
from random import shuffle, choices, random
from collections import namedtuple
# TODO Maybe move algorithm parameters to separate config file
POPULATION_SIZE = 20
GENERATION_COUNT = 20
SHUFFLE_NO = 3
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.1
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0
DEFAULT_FITNESS = 10000

Item = namedtuple("Item", ["row", "col", "value"])


class Generation():
    def __init__(self, size: int, board: Board):
        self._board = board
        self._size = size
        self._population = [self.generate_sample() for _ in range(self._size)]

    def generate_sample(self):
        def shuffle_sample():
            sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for _ in range(SHUFFLE_NO):
                shuffle(sample)
            return sample

        return [np.array([shuffle_sample() for _ in range(9)], dtype=np.int8),
                DEFAULT_FITNESS]

    def compute_chromosome_fitness(self, sample_no):
        def calc_penalty(sum_in_nine):
            return abs(45 - sum_in_nine)

        incorrect_fixed_value_penalty = 90
        fitness = 0
        sample = np.reshape(self._population[sample_no][0], (9, 9))
        v_calc_penalty = np.vectorize(calc_penalty)
        # incorrect sum in column
        fitness = np.sum(v_calc_penalty(np.sum(sample, axis=0)))
        # incorrect sum in row
        fitness += np.sum(v_calc_penalty(np.sum(sample, axis=1)))
        # incorrect sum in square
        # TODO try to vectorize it
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                fitness += abs(45 - np.sum(sample[row:row+3, col:col+3]))
        # incorrect known item
        for item in self._board.items:
            if sample[item.row, item.col] != item.value:
                fitness += incorrect_fixed_value_penalty

        self._population[sample_no][1] = fitness

    def _compute_population_fitness(self):
        def use_fitness(elem):
            return elem[1]
        for chromosome_no in range(self._size):
            self.compute_chromosome_fitness(chromosome_no)
        self._population.sort(key=use_fitness)

    def _get_elite(self):
        elite = []
        for chromosome_no in range(int(GENERATION_COUNT * ELITISM_COEFF)):
            elite.append([self._population[chromosome_no][0],
                          DEFAULT_FITNESS])
        return elite

    def _select_fittest(self):
        chromosome_count = int(GENERATION_COUNT * DROP_OUT_COEFF)
        fittest_count = int(GENERATION_COUNT * (1 - ELITISM_COEFF))
        fittest = choices(self._population[0:chromosome_count],
                          k=fittest_count)
        return [[item[0], DEFAULT_FITNESS] for item in fittest]

    def _create_child(self, parent1, parent2):
        # TODO Think how crossover point should look like!!!
        # Crossover point: split sudoku table in half horizontally
        new_child = [np.array([0 for _ in range(9)], dtype=np.int8),
                     DEFAULT_FITNESS]
        random_number = random()
        if random_number <= CROSSOVER_PROBABILITY:
            # upper part from parent1 and bottom from parent2
            pass
        elif random_number <= (2.0 * CROSSOVER_PROBABILITY):
            # upper part from parent2 and bottom from parent1
            pass
        else:
            # mutate but I don't know how!!!
            pass
        return new_child

    def evolve(self):
        new_population = []
        self._compute_population_fitness()
        # elitism
        new_population += self._get_elite()
        # selection
        fittest = self._select_fittest()
        # crossover
        # mutation
        self._population = fittest.copy()


class Board():
    def __init__(self):
        self._items = []

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

        self._items = board.copy()

if __name__ == "__main__":
    board = Board()
    board.inject_board()
    population = Generation(POPULATION_SIZE, board)
    population.evolve()
    for no in range(len(population._population)):
        print(f"Sample #{no} fitness = {population._population[no][1]}")
        print(population._population[no][0])
        print("-------------------------------------")
