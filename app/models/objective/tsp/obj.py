from typing import List, Any

from app.models.fitness.obj import Fitness
from app.models.objective.obj import Objective
from app.models.objective.tsp.base import TravelingSalesmanProblemObjectiveBase


class TravelingSalesmanProblemObjective(TravelingSalesmanProblemObjectiveBase, Objective):
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
