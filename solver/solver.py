import time
from solver.board import Board
from solver.generation import Generation


class GeneticSolver():
    def __init__(self,
                 board: Board,
                 population_size: int,
                 elitism: int,
                 drop_out: int,
                 crossover: int):
        self._board = board
        self._generation = Generation(population_size,
                                      self._board,
                                      elitism,
                                      drop_out,
                                      crossover)

    def run(self):
        max_no_of_generations = 10000
        generation_no = 0
        start_time = time.time()
        while generation_no <= max_no_of_generations:
            fittest = self._generation.evolve()
            if generation_no % 100 == 0:
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
            generation_no += 1
        stop_time = time.time()
        run_time = stop_time - start_time
        print(f"Solution couldn't be found in {generation_no - 1} generations")
        print(f"Fitnes of best solution: {fittest[1]}")
        print(fittest[0])
        print(f"Elapsed time: {run_time: .3f}s")
