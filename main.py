from solver.board import Board
from solver.generation import Generation
from solver.solver import GeneticSolver
# TODO Maybe move algorithm parameters to separate config file


if __name__ == "__main__":
    board = Board()
    board.inject_board()
    algorithm = GeneticSolver(board)
    algorithm.run()
