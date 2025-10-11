import random
from collections import deque
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.crossover.ox.base import OrderCrossoverBase


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class OrderCrossover(OrderCrossoverBase, Crossover):

    @staticmethod
    def _crossover(parent_1_encoding: List[int], parent_2_encoding: List[int], start_idx: int, end_idx: int) -> List[int]:
        size = len(parent_1_encoding)
        child_encoding = np.full(size, np.nan)

        # copy the subsequence from parent one
        child_encoding[start_idx:end_idx + 1] = parent_1_encoding[start_idx:end_idx + 1]

        # get remaining genes in the order starting at the end_idx
        remaining_gene_values = deque(
            [
                gene_value for gene_value in parent_2_encoding[end_idx + 1:] + parent_2_encoding[:end_idx + 1]
                if gene_value not in parent_1_encoding[start_idx:end_idx + 1]
            ]
        )

        for i in range(end_idx + 1, end_idx + size - (end_idx - start_idx)):
            idx = i % size
            child_encoding[idx] = remaining_gene_values.popleft()

        return child_encoding.tolist()

    def crossover_parents(self, parents: List[Individual], n_offspring: int) -> List[Individual]:
        offspring = []

        for _ in range(n_offspring // 2):
            parent_1_idx, parent_2_idx = random.sample(range(len(parents)), 2)
            parent_1_encoding = parents[parent_1_idx].encoding
            parent_2_encoding = parents[parent_2_idx].encoding

            if random.random() < self.crossover_probability:
                start_idx, end_idx = sorted(random.sample(range(len(parent_1_encoding)), 2))

                offspring.append(Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding, start_idx, end_idx)))
                offspring.append(Individual(encoding=self._crossover(parent_2_encoding, parent_1_encoding, start_idx, end_idx)))
            else:
                offspring.append(Individual(encoding=parent_1_encoding))
                offspring.append(Individual(encoding=parent_2_encoding))

        return offspring


def test():
    x = OrderCrossover(crossover_probability=1.0)
    parent_1_encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_2_encoding = [9, 3, 7, 8, 2, 6, 5, 1, 4]
    start_idx = 3
    end_idx = 6

    assert x._crossover(parent_1_encoding, parent_2_encoding, start_idx, end_idx) == [3, 8, 2, 4, 5, 6, 7, 1, 9]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    random.seed(1)

    offspring = x.crossover_parents(parents, 2)

    assert len(offspring) == 2

    for i, parent in enumerate(parents):
        assert offspring[i].encoding != parent.encoding

