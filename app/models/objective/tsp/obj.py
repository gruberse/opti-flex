from typing import List, Any

import numpy as np

from app.models.fitness.obj import Fitness
from app.models.objective.obj import Objective
from app.models.objective.tsp.base import TravelingSalesmanObjectiveBase


class TravelingSalesmanObjective(TravelingSalesmanObjectiveBase, Objective):
    matrix: Any = None

    def _get_fitness(self, encoding: List[int]) -> Fitness:
        fitness = 0

        for i in range(len(encoding) - 1):
            fitness = fitness + self.matrix[encoding[i]][encoding[i + 1]]

        fitness = fitness + self.matrix[encoding[len(encoding) - 1]][encoding[0]]

        return Fitness(objective_id=self.objective_id, actual_fitness=fitness)

    def init_evaluation_setup(self) -> None:
        if self.privacy_engine:
            raise RuntimeError('Privacy Engine is not supported.')


def test():
    objective = TravelingSalesmanObjective(objective_id="test", matrix=np.array([
        [0, 1, 2],
        [3, 0, 4],
        [5, 6, 0]
    ]))

    assert objective._get_fitness([0, 1, 2]).actual_fitness == 1 + 4 + 5
    assert objective._get_fitness([0, 2, 1]).actual_fitness == 2 + 6 + 3
    assert objective._get_fitness([1, 0, 2]).actual_fitness == 3 + 2 + 6
    assert objective._get_fitness([1, 2, 0]).actual_fitness == 4 + 5 + 1
    assert objective._get_fitness([2, 0, 1]).actual_fitness == 5 + 1 + 4
    assert objective._get_fitness([2, 1, 0]).actual_fitness == 6 + 3 + 2
