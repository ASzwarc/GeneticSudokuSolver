## First run
First run on simple sudoku. Algorithm didn't manage to find solution in 10000 generations. The best solution has score 56. I've noticed that numbers are not unique in rows, columns and squares. Fitness function doesn't have any penalty for such case.
Parameters:
- GENERATION_COUNT = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.1
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0
