import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.mutation.scramble.base import ScrambleMutationBase


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class ScrambleMutation(ScrambleMutationBase, Mutation):

    def _mutate(self, encoding: List[int], idx_1: int, idx_2: int) -> List[int]:
        subsequence = encoding[idx_1:idx_2 + 1]
        random.shuffle(subsequence)
        encoding[idx_1:idx_2 + 1] = subsequence
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
    m = ScrambleMutation(mutation_probability=1.0)
    encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx_1 = 1
    idx_2 = 4

    random.seed(14)
    assert m._mutate(encoding, idx_1, idx_2) == [1, 3, 5, 4, 2, 6, 7, 8, 9]

    offspring = [
        Individual(encoding=encoding),
    ]

    mutated_offspring = m.mutate_offspring(offspring)

    assert len(mutated_offspring) == 1

    for i, child in enumerate(offspring):
        assert mutated_offspring[i].encoding != child.encoding
