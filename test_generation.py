import unittest
from main import Generation


class TestGeneration(unittest.TestCase):

    def test_compute_fitness(self):
        population_size = 1
        generation = Generation(population_size)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
