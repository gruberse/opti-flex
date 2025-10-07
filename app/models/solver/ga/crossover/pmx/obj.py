import random
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.crossover.pmx.base import PartiallyMatchedCrossoverBase


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
class PartiallyMatchedCrossover(PartiallyMatchedCrossoverBase, Crossover):

    def _crossover(self, parent_1_encoding: List[int], parent_2_encoding: List[int], start_idx: int, end_idx: int) -> \
            List[int]:
        size = len(parent_1_encoding)
        child_encoding = np.full(size, np.nan)

        # copy the subsequence from parent one
        child_encoding[start_idx:end_idx] = parent_1_encoding[start_idx:end_idx]

        # build the mapping
        mapping = {parent_1_encoding[i]: parent_2_encoding[i] for i in range(start_idx, end_idx)}

        # fill the remaining positions
        for i in range(size):
            if not (start_idx <= i < end_idx):
                candidate = parent_2_encoding[i]
                # resolve conflicts via mapping
                while candidate in mapping:
                    candidate = mapping[candidate]
                child_encoding[i] = candidate

        return child_encoding.tolist()

    def crossover_parents(self, parents: List[Individual]) -> List[Individual]:
        offspring = []

        for i in range(0, len(parents), 2):
            parent_1_encoding = parents[i].encoding
            parent_2_encoding = parents[i + 1].encoding

            if random.random() < self.crossover_probability:
                start_idx, end_idx = sorted(random.sample(range(len(parent_1_encoding) + 1), 2))

                offspring.append(
                    Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding, start_idx, end_idx)))
                offspring.append(
                    Individual(encoding=self._crossover(parent_2_encoding, parent_1_encoding, start_idx, end_idx)))

            else:
                offspring.append(Individual(encoding=parent_1_encoding))
                offspring.append(Individual(encoding=parent_2_encoding))

        return offspring


def test():
    x = PartiallyMatchedCrossover(crossover_probability=1.0)
    parent_1_encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_2_encoding = [9, 3, 7, 8, 2, 6, 5, 1, 4]
    start_idx = 3
    end_idx = 7

    assert x._crossover(parent_1_encoding, parent_2_encoding, start_idx, end_idx) == [9, 3, 2, 4, 5, 6, 7, 1, 8]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    random.seed(1)
    np.random.seed(1)

    offspring = x.crossover_parents(parents)
    for i, parent in enumerate(parents):
        assert offspring[i].encoding != parent.encoding

