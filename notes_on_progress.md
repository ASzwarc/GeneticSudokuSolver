## Run #1
Algorithm didn't manage to find solution in 10000 generations. The best solution has score 56. I've noticed that numbers are not unique in rows, columns and squares. Fitness function doesn't have any penalty for such case.

Running time: no measurement

Parameters:
- GENERATION_COUNT = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.1
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #2
Fitness function was modified, penalty for duplication in row, column or square was added. Solution wasn't found in 10000 generations. Best result reached fitness 1648. It can't be compared to previous one because fitness function has changed.

Running time: 1070.115s

Parameters:
- GENERATION_COUNT = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.1
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0
