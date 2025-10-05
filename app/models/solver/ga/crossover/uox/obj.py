import random
from collections import deque
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.crossover.uox.base import UniformOrderBasedCrossoverBase


# based on "Computational Intelligence" by Kruse et al. (2022)
class UniformOrderBasedCrossover(UniformOrderBasedCrossoverBase, Crossover):

    def _crossover(self, parent_1_encoding: List[int], parent_2_encoding: List[int], mask: np.ndarray) -> List[int]:
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

    def crossover_parents(self, parents: List[Individual]) -> List[Individual]:
        offspring = []

        for i in range(0, len(parents), 2):
            parent_1_encoding = parents[i].encoding
            parent_2_encoding = parents[i + 1].encoding

            if random.random() < self.crossover_probability:
                mask = np.random.rand(len(parents[0].encoding)) <= self.keep_genes_probability
                if isinstance(mask, float):
                    mask = np.array([mask])

                offspring.append(Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding, mask)))
                offspring.append(Individual(encoding=self._crossover(parent_2_encoding, parent_1_encoding, mask)))

            else:
                offspring.append(Individual(encoding=parent_1_encoding))
                offspring.append(Individual(encoding=parent_2_encoding))

        return offspring


def test():
    uox = UniformOrderBasedCrossover(crossover_probability=1.0, keep_genes_probability=0.00001)
    parent_1_encoding = [5, 7, 2, 4, 6, 3, 1]
    parent_2_encoding = [4, 2, 3, 1, 5, 7, 6]
    mask = np.array([True, False, True, True, False, False, True])

    result = uox._crossover(
        parent_1_encoding=parent_1_encoding,
        parent_2_encoding=parent_2_encoding,
        mask=mask
    )
    assert result == [5, 3, 2, 4, 7, 6, 1]

    result = uox._crossover(
        parent_1_encoding=parent_2_encoding,
        parent_2_encoding=parent_1_encoding,
        mask=mask
    )
    assert result == [4, 5, 3, 1, 7, 2, 6]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    result = uox.crossover_parents(parents)
    for i, parent in enumerate(parents):
        assert result[i].encoding != parent.encoding