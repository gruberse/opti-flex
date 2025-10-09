import random
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.ex.base import EdgeCrossoverBase
from app.models.solver.ga.crossover.obj import Crossover


class EdgeCrossover(EdgeCrossoverBase, Crossover):

    def _crossover(self, parent_1_encoding: List[int], parent_2_encoding: List[int]) -> List[int]:
        n_genes = len(parent_1_encoding)

        child_encoding = []

        # construct the edge table
        edge_table = {gene: [] for gene in parent_1_encoding}
        for encoding in [parent_1_encoding, parent_2_encoding]:
            for i in range(n_genes):
                gene = encoding[i]
                # left
                edge_table[gene].append(encoding[(i - 1) % n_genes])
                # right
                edge_table[gene].append(encoding[(i + 1) % n_genes])

        # pick a random start element
        current_element = random.choice(list(edge_table.keys()))
        child_encoding.append(current_element)

        while len(child_encoding) < n_genes:

            # remove the references to the current element
            for edges in edge_table.values():
                edges[:] = [edge for edge in edges if edge != current_element]

            # select the next element

            # in the case of an empty list, choose the next element at random
            options = edge_table[current_element]
            if len(options) == 0:
                print('empty')
                next_element = random.choice([gene for gene in edge_table.keys()])

            else:
                # option 1: select a common edge
                common_edges = set([edge for edge in options if options.count(edge) > 1])
                if len(common_edges) > 0:
                    next_element = random.choice(list(common_edges))

                else:
                    # option 2: select the element with the shortest list
                    shortest_list_length = min(
                        [len(set(edge_table[edge])) for edge in options],
                        default=0
                    )

                    shortest_list_edges = [
                        edge for edge in options
                        if len(set(edge_table[edge])) == shortest_list_length
                    ]

                    next_element = random.choice(shortest_list_edges)

            child_encoding.append(next_element)
            del edge_table[current_element]

            current_element = next_element

        return child_encoding

    def crossover_parents(self, parents: List[Individual], population_size: int) -> List[Individual]:
        offspring = []

        for i in range(2):
            for j in range(0, population_size, 2):
                parent_1_encoding = parents[j].encoding
                parent_2_encoding = parents[j + 1].encoding

                if random.random() < self.crossover_probability:
                    offspring.append(Individual(encoding=self._crossover(parent_1_encoding, parent_2_encoding)))

                else:
                    offspring.append(Individual(encoding=parent_1_encoding))
                    offspring.append(Individual(encoding=parent_2_encoding))

            random.shuffle(parents)

        return offspring


def test():
    x = EdgeCrossover(crossover_probability=1.0)
    parent_1_encoding = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent_2_encoding = [9, 3, 7, 8, 2, 6, 5, 1, 4]

    random.seed(2)

    print(x._crossover(parent_1_encoding, parent_2_encoding))

    parent_1 = [1, 2, 3, 4, 5, 6]
    parent_2 = [1, 3, 2, 6, 5, 4]

    print(x._crossover(parent_1, parent_2))