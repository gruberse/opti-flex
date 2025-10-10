import random
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.cx.base import CycleCrossoverBase
from app.models.solver.ga.crossover.obj import Crossover


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class CycleCrossover(CycleCrossoverBase, Crossover):
    def _crossover(self, parent_1_encoding: List[int], parent_2_encoding: List[int]) -> List[int]:

        child_encoding = np.full(len(parent_1_encoding), np.nan)
        p1 = np.array(parent_1_encoding)
        p2 = np.array(parent_2_encoding)

        while np.any(np.isnan(child_encoding)):
            i = np.where(np.isnan(child_encoding))[0][0]

            while True:
                gene_value = p1[i]
                child_encoding[i] = gene_value
                i = np.where(p2 == gene_value)[0]

                # cycle finished
                if not np.isnan(child_encoding[i]):
                    break

            # reverse order of parent solutions for the next cycle
            p1, p2 = p2, p1

        return child_encoding.tolist()

    def crossover_parents(self, parents: List[Individual], population_size: int) -> List[Individual]:
        offspring = []

        for _ in range(population_size // 2):
            parent_1_idx, parent_2_idx = random.sample(range(len(parents)), 2)
            parent_1_encoding = parents[parent_1_idx].encoding
            parent_2_encoding = parents[parent_2_idx].encoding

            if random.random() < self.crossover_probability:
                offspring.append(Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding)))
                offspring.append(Individual(encoding=self._crossover(parent_2_encoding, parent_1_encoding)))
            else:
                offspring.append(Individual(encoding=parent_1_encoding))
                offspring.append(Individual(encoding=parent_2_encoding))

        return offspring

def test():
    x = CycleCrossover(crossover_probability=1.0)
    parent_1_encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_2_encoding = [9, 3, 7, 8, 2, 6, 5, 1, 4]

    assert x._crossover(parent_1_encoding, parent_2_encoding) == [1, 3, 7, 4, 2, 6, 5, 8, 9]
    assert x._crossover(parent_2_encoding, parent_1_encoding) == [9, 2, 3, 8, 5, 6, 7, 1, 4]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    offspring = x.crossover_parents(parents, 2)
    for i, parent in enumerate(parents):
        assert offspring[i].encoding != parent.encoding
