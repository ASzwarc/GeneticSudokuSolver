## Run #1
Algorithm didn't manage to find solution in 10000 generations. The best solution has score 56. I've noticed that numbers are not unique in rows, columns and squares. Fitness function doesn't have any penalty for such case.

Running time: no measurement
<br>Best score: 56

Parameters:
- GENERATION_COUNT = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.1
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #2
Fitness function was modified, penalty for duplication in row, column or square was added. Solution wasn't found in 10000 generations. Best result reached fitness 1648. It can't be compared to previous one because fitness function has changed.

Running time: 1070.115s
<br>Best score: 1648

Parameters:
- GENERATION_COUNT = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.1
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #3

Running time: 176.344s
<br>Best score: 1688

Parameters:
- POPULATION_SIZE = 40
- ELITISM_COEFF = 0.2
- DROP_OUT_COEFF = 0.4
- MUTATION_PROBABILITY = 0.3
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #4
Changed crossover point - instead of row it's cell.

Running time: 92.762s
<br>Best score: 3120

- POPULATION_SIZE = 20
- ELITISM_COEFF = 0.1
- DROP_OUT_COEFF = 0.5
- MUTATION_PROBABILITY = 0.2
- CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #5
Changed crossover point - instead of row it's square.

Running time: 137.605s
<br>Best score: 2000

MAX_GENERATIONS = 10000
POPULATION_SIZE = 20
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #6
Changed crossover point - row.

Running time: 265.842s
<br>Best score: 1562

MAX_GENERATIONS = 10000
POPULATION_SIZE = 20
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #7
Changed crossover point - row.

Running time: 282.926s
<br>Best score: 2430

MAX_GENERATIONS = 10000
POPULATION_SIZE = 40
ELITISM_COEFF = 0.05
DROP_OUT_COEFF = 0.7
MUTATION_PROBABILITY = 0.3
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0

## Run #8
New approach - fixed values are not guessed. Row as a crossover point. It looks like something is not working as it should...

Running time: 214.787s
<br>Best score: 4369

MAX_GENERATIONS = 10000
POPULATION_SIZE = 40
ELITISM_COEFF = 0.1
DROP_OUT_COEFF = 0.5
MUTATION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = (1.0 - MUTATION_PROBABILITY) / 2.0