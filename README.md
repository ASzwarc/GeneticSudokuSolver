# GeneticSudokuSolver
[![Build Status](https://travis-ci.org/ASzwarc/GeneticSudokuSolver.svg?branch=master)](https://travis-ci.org/ASzwarc/GeneticSudokuSolver)

Goal of this project is to create genetic algorithm which will solve sudoku. I have never written genetic algorithm before so this should be fun...

# Found issues
- For some reason genetic algorithm doesn't work (I know that it's not the best algorithm for problems
like that...)
- Adding new sudoku board is annoying. It would be better if used could provide screenshot of the board and
program would "read" the board and inject data into program.

# TODO
## Algorithm
- [x] Basic structure
- [x] Generation of Sudoku board
- [x] Fitness function
- [x] Genetic algorithm
- [ ] Some kind of visualisation

## Model
- [ ] Algorithm that will detect single cell in screenshot of sudoku board.
- [ ] Create separate images for each cell that has same format as MNIST dataset.
- [ ] Model architecture for recognizing digits.
- [ ] Training model.
- [ ] Formatting output so it can be injected into code.
- [ ] CLI interface for running whole program.