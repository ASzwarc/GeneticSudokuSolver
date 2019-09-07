import unittest
from main import Generation, Board
import numpy as np


class TestComputeFitness(unittest.TestCase):
    def setUp(self):
        self.population_size = 1
        self.generation = Generation(self.population_size)

    def test_values_in_rows_and_columns_incorrect(self):
        board = Board()
        sample_no = 0
        self.generation._population[sample_no] = np.array(
            [1 for _ in range(81)], dtype=np.int8)
        self.assertEqual(972,
                         self.generation.compute_fitness(sample_no, board))

    def test_values_in_rows_and_columns_correct(self):
        board = Board()
        sample_no = 0
        sample = [1, 5, 2, 4, 8, 9, 3, 7, 6,
                  7, 3, 9, 2, 5, 6, 8, 4, 1,
                  4, 6, 8, 3, 7, 1, 2, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  5, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 1, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 4]
        self.generation._population[sample_no] = np.array(
            sample, dtype=np.int8)
        self.assertEqual(0,
                         self.generation.compute_fitness(sample_no, board))

if __name__ == '__main__':
    unittest.main()
