import time
from solver.board import Board
from solver.generation import Generation
# TODO Maybe move algorithm parameters to separate config file
POPULATION_SIZE = 20
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.1
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0


class GeneticSolution():
    def __init__(self, board: Board):
        self._board = board
        self._generation = Generation(POPULATION_SIZE,
                                      self._board,
                                      ELITISM_COEFF,
                                      DROP_OUT_COEFF,
                                      CROSSOVER_PROBABILITY)

    def run(self):
        max_no_of_generations = 10000
        generation_no = 0
        start_time = time.time()
        while generation_no <= max_no_of_generations:
            fittest = self._generation.evolve()
            generation_no += 1
            print("-------------------------------------")
            print(f"Generation {generation_no} - fittest {fittest[1]}")
            print("-------------------------------------")
            if fittest[1] == 0:
                stop_time = time.time()
                run_time = stop_time - start_time
                print(f"Solution found in {generation_no} generations!")
                print(fittest[0])
                print(f"Elapsed time: {run_time: .3f}s")
                return
        stop_time = time.time()
        run_time = stop_time - start_time
        print(f"Solution couldn't be found in {generation_no} generations")
        print(f"Fitnes of best solution: {fittest[1]}")
        print(fittest[0])
        print(f"Elapsed time: {run_time: .3f}s")

if __name__ == "__main__":
    board = Board()
    board.inject_board()
    algorithm = GeneticSolution(board)
    algorithm.run()
