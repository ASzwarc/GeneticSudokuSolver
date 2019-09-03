import numpy as np

# TODO Maybe move algorithm parameters to separate config file
POPULATION_SIZE = 20
GENERATION_COUNT = 20


# Genetic algorithm:
# 1. generate initial population
# 2. compute fitness
# 3. LOOP: selection, crossover, mutation, compute fitness

class Population():
    def __init__(self, size):
        def generate_sample():
            pass
        self._population = np.array([generate_sample() for _ in range(
                                        POPULATION_SIZE)])


class Board():
    def __init__(self):
        self._matrix = np.array([[-1 for _ in range(9)] for _ in range(9)],
                                dtype=np.int8)

    def inject_board(self):
        """
        Helper function for injecting solvable sudoku board.
        Board taken from this page, section "Easiest":
        https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
        """
        # TODO: Think about way to inject or generate boards
        self._matrix[0, 3] = 2
        self._matrix[0, 4] = 6
        self._matrix[0, 6] = 7
        self._matrix[0, 8] = 1

        self._matrix[1, 0] = 6
        self._matrix[1, 1] = 8
        self._matrix[1, 4] = 7
        self._matrix[1, 7] = 9

        self._matrix[2, 0] = 1
        self._matrix[2, 1] = 9
        self._matrix[2, 5] = 4
        self._matrix[2, 6] = 5

        self._matrix[3, 0] = 8
        self._matrix[3, 1] = 2
        self._matrix[3, 3] = 1
        self._matrix[3, 7] = 4

        self._matrix[4, 2] = 4
        self._matrix[4, 3] = 6
        self._matrix[4, 5] = 2
        self._matrix[4, 6] = 9

        self._matrix[5, 1] = 5
        self._matrix[5, 5] = 3
        self._matrix[5, 7] = 2
        self._matrix[5, 8] = 8

        self._matrix[6, 2] = 9
        self._matrix[6, 3] = 3
        self._matrix[6, 7] = 7
        self._matrix[6, 8] = 4

        self._matrix[7, 1] = 4
        self._matrix[7, 4] = 5
        self._matrix[7, 7] = 3
        self._matrix[7, 8] = 6

        self._matrix[8, 0] = 7
        self._matrix[8, 2] = 3
        self._matrix[8, 4] = 1
        self._matrix[8, 5] = 8

if __name__ == "__main__":
    board = Board()
    print(board._matrix)
    board.inject_board()
    print(board._matrix)
