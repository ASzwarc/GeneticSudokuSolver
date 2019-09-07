import unittest
from main import Generation, Board, Item
import numpy as np


# TODO refactor this tests!!!
class TestComputeFitness(unittest.TestCase):
    def setUp(self):
        self.population_size = 1
        self.generation = Generation(self.population_size)
        self.sample_no = 0
        self.board = Board()

    def test_values_in_rows_and_columns_incorrect(self):
        self.generation._population[self.sample_no] = np.array(
            [1 for _ in range(81)], dtype=np.int8)
        self.assertEqual(972,
                         self.generation.compute_fitness(self.sample_no,
                                                         self.board))

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
        self.generation._population[self.sample_no] = np.array(
            sample, dtype=np.int8)
        self.assertEqual(
            0, self.generation.compute_fitness(self.sample_no, self.board))

    def test_known_values_incorrect(self):
        known_items = []
        known_items.append(Item._make([0, 0, 1]))
        known_items.append(Item._make([0, 3, 4]))
        known_items.append(Item._make([0, 8, 6]))
        known_items.append(Item._make([1, 1, 3]))
        known_items.append(Item._make([1, 4, 5]))
        known_items.append(Item._make([1, 7, 4]))
        known_items.append(Item._make([2, 2, 8]))
        known_items.append(Item._make([2, 5, 1]))
        known_items.append(Item._make([2, 6, 2]))
        known_items.append(Item._make([4, 0, 5]))
        known_items.append(Item._make([6, 1, 1]))
        known_items.append(Item._make([8, 8, 4]))
        self.board._items = known_items

        sample = [9, 5, 2, 5, 8, 9, 3, 7, 1,
                  7, 1, 9, 2, 9, 6, 8, 3, 1,
                  4, 6, 1, 3, 7, 9, 1, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  1, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 9, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 1]
        self.generation._population[self.sample_no] = np.array(
            sample, dtype=np.int8)
        self.assertEqual(
            0, self.generation.compute_fitness(self.sample_no, self.board))

    def test_known_values_correct(self):
        known_items = []
        known_items.append(Item._make([0, 0, 1]))
        known_items.append(Item._make([0, 3, 4]))
        known_items.append(Item._make([0, 8, 6]))
        known_items.append(Item._make([1, 1, 3]))
        known_items.append(Item._make([1, 4, 5]))
        known_items.append(Item._make([1, 7, 4]))
        known_items.append(Item._make([2, 2, 8]))
        known_items.append(Item._make([2, 5, 1]))
        known_items.append(Item._make([2, 6, 2]))
        known_items.append(Item._make([4, 0, 5]))
        known_items.append(Item._make([6, 1, 1]))
        known_items.append(Item._make([8, 8, 4]))
        self.board._items = known_items

        sample = [1, 5, 2, 4, 8, 9, 3, 7, 6,
                  7, 3, 9, 2, 5, 6, 8, 4, 1,
                  4, 6, 8, 3, 7, 1, 2, 9, 5,
                  3, 8, 7, 1, 2, 4, 6, 5, 9,
                  5, 9, 1, 7, 6, 3, 4, 2, 8,
                  2, 4, 6, 8, 9, 5, 7, 1, 3,
                  9, 1, 4, 6, 3, 7, 5, 8, 2,
                  6, 2, 5, 9, 4, 8, 1, 3, 7,
                  8, 7, 3, 5, 1, 2, 9, 6, 4]
        self.generation._population[self.sample_no] = np.array(
            sample, dtype=np.int8)
        self.assertEqual(
            0, self.generation.compute_fitness(self.sample_no, self.board))

if __name__ == '__main__':
    unittest.main()
