import unittest
from solver.generation import Generation
from solver.board import Board
import numpy as np


def dummy_crossover_function(parent1, parent2, cross_probability: float):
    return None


class TestComputeFitness(unittest.TestCase):
    def setUp(self):
        self.ELITE_COEFF = 1
        self.DROP_OUT_COEFF = 1
        self.CROSSOVER = 1
        self.population_size = 1
        self.board = Board()
        self.generation = Generation(self.population_size,
                                     self.board,
                                     self.ELITE_COEFF,
                                     self.DROP_OUT_COEFF,
                                     self.CROSSOVER,
                                     dummy_crossover_function)
        self.sample_no = 0
        self.DEFAULT_FITNESS = 10000

    def test_values_in_rows_and_columns_incorrect(self):
        self.generation._population[self.sample_no] = [np.array(
            [1 for _ in range(81)], dtype=np.int8), self.DEFAULT_FITNESS]
        self.generation.compute_chromosome_fitness(self.sample_no)
        self.assertEqual(9612,
                         self.generation._population[self.sample_no][1])

        self.generation._population[self.sample_no] = [np.array(
            [9 for _ in range(81)], dtype=np.int8), self.DEFAULT_FITNESS]
        self.generation.compute_chromosome_fitness(self.sample_no)
        self.assertEqual(9612,
                         self.generation._population[self.sample_no][1])

    def test_values_in_rows_and_columns_correct(self):
        sample = [1, 5, 2, 4, 8, 9, 3, 7, 6,
                  7, 3, 9, 2, 5, 6, 8, 4, 1,
                  4, 6, 8, 3, 7, 1, 2, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  5, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 1, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 4]
        self.generation._population[self.sample_no] = [np.array(
            sample, dtype=np.int8), self.DEFAULT_FITNESS]
        self.generation.compute_chromosome_fitness(self.sample_no)
        self.assertEqual(
            0, self.generation._population[self.sample_no][1])

    def test_known_values_incorrect(self):
        known_items = []
        known_items.append([1, 0, 0, 4, 0, 0, 0, 0, 6])
        known_items.append([0, 3, 0, 0, 5, 0, 0, 4, 0])
        known_items.append([0, 0, 8, 0, 0, 1, 2, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([5, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 1, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 4])
        self.board._board = known_items

        sample = [9, 5, 2, 5, 8, 9, 3, 7, 1,
                  7, 1, 9, 2, 9, 6, 8, 3, 1,
                  4, 6, 1, 3, 7, 9, 1, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  1, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 9, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 1]
        self.generation._population[self.sample_no] = [np.array(
            sample, dtype=np.int8), self.DEFAULT_FITNESS]
        self.generation.compute_chromosome_fitness(self.sample_no)
        self.assertEqual(
            2336, self.generation._population[self.sample_no][1])

    def test_known_values_correct(self):
        known_items = []
        known_items.append([1, 0, 0, 4, 0, 0, 0, 0, 6])
        known_items.append([0, 3, 0, 0, 5, 0, 0, 4, 0])
        known_items.append([0, 0, 8, 0, 0, 1, 2, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([5, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 1, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        known_items.append([0, 0, 0, 0, 0, 0, 0, 0, 4])
        self.board._board = known_items

        sample = [1, 5, 2, 4, 8, 9, 3, 7, 6,
                  7, 3, 9, 2, 5, 6, 8, 4, 1,
                  4, 6, 8, 3, 7, 1, 2, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  5, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 1, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 4]
        self.generation._population[self.sample_no] = [np.array(
            sample, dtype=np.int8), self.DEFAULT_FITNESS]
        self.generation.compute_chromosome_fitness(self.sample_no)
        self.assertEqual(
            0, self.generation._population[self.sample_no][1])

if __name__ == '__main__':
    unittest.main()
