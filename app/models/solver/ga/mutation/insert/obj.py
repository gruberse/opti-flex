import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.insert.base import InsertMutationBase
from app.models.solver.ga.mutation.obj import Mutation


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class InsertMutation(InsertMutationBase, Mutation):

    def _mutate(self, encoding: List[int], idx_1: int, idx_2: int) -> List[int]:
        gene_value = encoding.pop(idx_1)
        if idx_1 < idx_2:
            idx_2 -= 1
        encoding.insert(idx_2, gene_value)
        return encoding


    def mutate_offspring(self, offspring: List[Individual]) -> List[Individual]:
        mutated_offspring = []

        for i in range(len(offspring)):

            if random.random() < self.mutation_probability:
                encoding = offspring[i].encoding.copy()

                idx_1, idx_2 = random.sample(range(len(encoding)), 2)

                encoding = self._mutate(encoding, idx_1, idx_2)

                mutated_offspring.append(Individual(encoding=encoding))

            else:
                mutated_offspring.append(offspring[i])

        return mutated_offspring


def test():
    m = InsertMutation(mutation_probability=1.0)
    encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    idx_1 = 4
    idx_2 = 2

    assert m._mutate(encoding, idx_1, idx_2) == [1, 2, 5, 3, 4, 6, 7, 8, 9]

    offspring = [
        Individual(encoding=encoding),
    ]

    random.seed(1)

    mutated_offspring = m.mutate_offspring(offspring)

    assert len(mutated_offspring) == 1

    for i, child in enumerate(offspring):
        assert mutated_offspring[i].encoding != child.encoding
