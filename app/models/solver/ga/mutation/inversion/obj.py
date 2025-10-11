import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.inversion.base import InversionMutationBase
from app.models.solver.ga.mutation.obj import Mutation


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class InversionMutation(InversionMutationBase, Mutation):

    @staticmethod
    def _mutate(encoding: List[int], idx_1: int, idx_2: int) -> List[int]:
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
    m = InversionMutation(mutation_probability=1.0)
    encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx_1 = 1
    idx_2 = 4

    assert m._mutate(encoding, idx_1, idx_2) == [1, 5, 4, 3, 2, 6, 7, 8, 9]

    offspring = [
        Individual(encoding=encoding),
    ]

    random.seed(1)

    mutated_offspring = m.mutate_offspring(offspring)

    assert len(mutated_offspring) == 1

    for i, child in enumerate(offspring):
        assert mutated_offspring[i].encoding != child.encoding
