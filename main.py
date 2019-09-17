from solver.board import Board
from solver.solver import GeneticSolver
import solver.crossover_functions

MAX_GENERATIONS = 10000
POPULATION_SIZE = 40
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

if __name__ == "__main__":
    board = Board()
    board.inject_board()
    algorithm = GeneticSolver(board,
                              MAX_GENERATIONS,
                              POPULATION_SIZE,
                              ELITISM_COEFF,
                              DROP_OUT_COEFF,
                              CROSSOVER_PROBABILITY,
                              solver.crossover_functions.row_crossover)
    algorithm.run()
