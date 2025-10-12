import random
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.erx.base import EdgeRecombinationCrossoverBase
from app.models.solver.ga.crossover.obj import Crossover


# based on "Introduction to Evolutionary Computation" by Eiben and Smith (2015)
# based on "Computational Intelligence" by Kruse et al. (2022)
class EdgeRecombinationCrossover(EdgeRecombinationCrossoverBase, Crossover):

    @staticmethod
    def _crossover(parent_1_encoding: List[int], parent_2_encoding: List[int]) -> List[int]:
        n_genes = len(parent_1_encoding)

        child_encoding = []

        # construct the edge table
        #   the first set collects neighbor edges
        #   the second set collects common neighbor edges
        edge_table = {element: (set(), set()) for element in parent_1_encoding}

        for encoding in [parent_1_encoding, parent_2_encoding]:

            for i in range(n_genes):
                element = encoding[i]

                for neighbor in [encoding[(i - 1) % n_genes], encoding[(i + 1) % n_genes]]:
                    if neighbor in edge_table[element][0]:
                        edge_table[element][0].discard(neighbor)
                        edge_table[element][1].add(neighbor)
                    else:
                        edge_table[element][0].add(neighbor)

        # start from a random gene
        current_element = random.choice(list(edge_table.keys()))
        child_encoding.append(current_element)

        while len(child_encoding) < n_genes:

            # remove the references to the current element
            for neighbors, common_neighbors in edge_table.values():
                neighbors.discard(current_element)
                common_neighbors.discard(current_element)

            # select the next element
            neighbor_list = edge_table[current_element]
            del edge_table[current_element]

            # option 3: select a random gene value
            if len(neighbor_list[0]) == 0 and len(neighbor_list[1]) == 0:
                next_element = random.choice([element for element in edge_table.keys()])

            # option 1: select a common edge
            elif len(neighbor_list[1]) > 0:
                next_element = random.choice([element for element in neighbor_list[1]])

            # option 2: shortest neighborhood list
            else:
                shortest_list_length = min(
                    [len(edge_table[neighbor][0]) + len(edge_table[neighbor][1])
                     for neighbor in neighbor_list[0]],
                    default=0
                )

                shortest_list_edges = [
                    neighbor for neighbor in neighbor_list[0]
                    if len(edge_table[neighbor][0]) + len(edge_table[neighbor][1]) == shortest_list_length
                ]

                next_element = random.choice(shortest_list_edges)

            current_element = next_element
            child_encoding.append(current_element)

        return child_encoding

    def crossover_parents(self, parents: List[Individual], n_offspring: int) -> List[Individual]:
        offspring = []

        while len(offspring) < n_offspring:
            parent_1_idx, parent_2_idx = sorted(random.sample(range(len(parents)), 2))
            parent_1_encoding = parents[parent_1_idx].encoding
            parent_2_encoding = parents[parent_2_idx].encoding

            if random.random() < self.crossover_probability:
                offspring.append(Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding)))
            else:
                offspring.append(Individual(encoding=parent_1_encoding))

        return offspring


def test():
    x = EdgeRecombinationCrossover(crossover_probability=1.0)
    parent_1_encoding = [6, 3, 1, 5, 2, 7, 4]
    parent_2_encoding = [3, 7, 2, 5, 6, 1, 4]

    random.seed(57)

    assert x._crossover(parent_1_encoding, parent_2_encoding) == [6, 5, 2, 7, 4, 3, 1]

    random.seed(86)

    parent_1_encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_2_encoding = [9, 3, 7, 8, 2, 6, 5, 1, 4]

    assert x._crossover(parent_1_encoding, parent_2_encoding) == [1, 5, 6, 2, 8, 7, 3, 9, 4]

    parents = [
        Individual(encoding=parent_1_encoding),
        Individual(encoding=parent_2_encoding),
    ]

    offspring = x.crossover_parents(parents, 2)

    assert len(offspring) == 2

    for i, parent in enumerate(parents):
        assert offspring[i].encoding != parent.encoding
