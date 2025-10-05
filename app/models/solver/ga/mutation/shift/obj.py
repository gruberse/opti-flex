import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.mutation.shift.base import ShiftMutationBase


# based on "Computational Intelligence" by Kruse et al. (2022)
class ShiftMutation(ShiftMutationBase, Mutation):
    def _mutate(self, encoding: List[int], idx_1: int, idx_2: int, insertion_idx: int) -> List[int]:
        subsequence = encoding[idx_1:idx_2]
        encoding = encoding[:idx_1] + encoding[idx_2:]
        encoding = encoding[:insertion_idx] + subsequence + encoding[insertion_idx:]
        return encoding


    def mutate_offspring(self, offspring: List[Individual]) -> List[Individual]:
        mutated_offspring = []

        for i in range(len(offspring)):

            if random.random() < self.mutation_probability:

                encoding = offspring[i].encoding.copy()

                idx_1, idx_2 = sorted(random.sample(range(len(encoding)), 2))

                insertion_idx = random.randint(0, len(encoding) - (idx_2 - idx_1))

                encoding = self._mutate(encoding, idx_1, idx_2, insertion_idx)

                mutated_offspring.append(Individual(encoding=encoding))

            else:
                mutated_offspring.append(offspring[i])

        return mutated_offspring


def test():
    sm = ShiftMutation(mutation_probability=1.0)
    encoding = [3, 1, 4, 2, 5, 4, 6]
    idx_1 = 1
    idx_2 = 3
    insertion_idx = 3

    result = sm._mutate(encoding, idx_1, idx_2, insertion_idx)
    assert result == [3, 2, 5, 1, 4, 4, 6]

    offspring = [
        Individual(encoding=encoding),
    ]

    result = sm.mutate_offspring(offspring)
    for i, child in enumerate(offspring):
        assert result[i].encoding != child.encoding
