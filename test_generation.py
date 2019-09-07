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
        self.assertEqual(972, self.generation.compute_fitness(sample_no, board))

if __name__ == '__main__':
    unittest.main()
