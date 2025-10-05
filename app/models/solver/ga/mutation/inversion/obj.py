import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.inversion.base import InversionMutationBase
from app.models.solver.ga.mutation.obj import Mutation


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class InversionMutation(InversionMutationBase, Mutation):
    def _mutate(self, encoding: List[int], idx_1: int, idx_2: int) -> List[int]:
        encoding[idx_1:idx_2 + 1] = encoding[idx_1:idx_2 + 1][::-1]
        return encoding

    def mutate_offspring(self, offspring: List[Individual]) -> List[Individual]:
        mutated_offspring = []

        for i in range(len(offspring)):

            if random.random() < self.mutation_probability:
                encoding = offspring[i].encoding.copy()

                idx_1, idx_2 = sorted(random.sample(range(len(encoding)), 2))

                encoding = self._mutate(encoding, idx_1, idx_2)

                mutated_offspring.append(Individual(encoding=encoding))

            else:
                mutated_offspring.append(offspring[i])

        return mutated_offspring

def test():
    im = InversionMutation(mutation_probability=1.0)
    encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx_1 = 1
    idx_2 = 4

    result = im._mutate(encoding, idx_1, idx_2)
    assert result == [1, 5, 4, 3, 2, 6, 7, 8, 9]

    offspring = [
        Individual(encoding=encoding),
    ]

    result = im.mutate_offspring(offspring)
    for i, child in enumerate(offspring):
        assert result[i].encoding != child.encoding
