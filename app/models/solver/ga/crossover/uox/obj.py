import random
from collections import deque
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.crossover.uox.base import UniformOrderBasedCrossoverBase


# based on "Computational Intelligence" by Kruse et al. (2022)
class UniformOrderBasedCrossover(UniformOrderBasedCrossoverBase, Crossover):

    @staticmethod
    def _crossover(parent_1_encoding: List[int], parent_2_encoding: List[int], mask: np.ndarray) -> List[int]:
        # initialize the encoding of the child with NaN
        child_encoding = np.full(len(parent_1_encoding), np.nan)
        used_gene_values = set()

        # set the gene values of parent one based on the mask
        for i in range(len(parent_1_encoding)):
            if mask[i]:
                child_encoding[i] = parent_1_encoding[i]
                used_gene_values.add(parent_1_encoding[i])

        # fill the remaining gene values in the order of parent two
        remaining_gene_values = deque([gene_value for gene_value in parent_2_encoding if gene_value not in used_gene_values])
        for i in range(len(parent_1_encoding)):
            if not mask[i]:
                child_encoding[i] = remaining_gene_values.popleft()

        return child_encoding.tolist()

    def crossover_parents(self, parents: List[Individual], n_offspring) -> List[Individual]:
        offspring = []

        while len(offspring) < n_offspring:
            parent_1_idx, parent_2_idx = random.sample(range(len(parents)), 2)
            parent_1_encoding = parents[parent_1_idx].encoding
            parent_2_encoding = parents[parent_2_idx].encoding

            if random.random() < self.crossover_probability:
                mask = np.random.rand(len(parents[0].encoding)) <= self.keep_genes_probability
                if isinstance(mask, float):
                    mask = np.array([mask])

                new_offspring = [
                    Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding, mask)),
                    Individual(encoding=self._crossover(parent_2_encoding, parent_1_encoding, mask))
                ]
            else:
                new_offspring = [
                    Individual(encoding=parent_1_encoding),
                    Individual(encoding=parent_2_encoding)
                ]

            offspring.extend(new_offspring[:n_offspring - len(offspring)])

        return offspring


def test():
    x = UniformOrderBasedCrossover(crossover_probability=1.0, keep_genes_probability=0.5)
    parent_1_encoding = [5, 7, 2, 4, 6, 3, 1]
    parent_2_encoding = [4, 2, 3, 1, 5, 7, 6]
    mask = np.array([True, False, True, True, False, False, True])

    assert x._crossover(
        parent_1_encoding=parent_1_encoding,
        parent_2_encoding=parent_2_encoding,
        mask=mask
    ) == [5, 3, 2, 4, 7, 6, 1]

    assert x._crossover(
        parent_1_encoding=parent_2_encoding,
        parent_2_encoding=parent_1_encoding,
        mask=mask
    ) == [4, 5, 3, 1, 7, 2, 6]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    random.seed(3)
    np.random.seed(3)

    offspring = x.crossover_parents(parents, 2)

    assert len(offspring) == 2

    for i, parent in enumerate(parents):
        assert offspring[i].encoding != parent.encoding