from typing import List

from app.models.individual.obj import Individual
from app.models.objective.tsp.obj import TravelingSalesmanProblemObjective
from app.models.problem.obj import Problem
from app.models.problem.tsp.base import TravelingSalesmanProblemBase
from app.models.problem.tsp.tour.obj import Tour


class TravelingSalesmanProblem(TravelingSalesmanProblemBase, Problem):
    objectives: List[TravelingSalesmanProblemObjective]
    result_tours: List[Tour] = []

    def __init__(self, /, **data):
        super().__init__(**data)

        self.nodes = sorted(self.nodes, key=lambda node: node.node_id)

        for objective in self.objectives:
            objective.init_evaluation_setup()

    def update_result(self, individuals: List[Individual]) -> None:
        self.result_tours = [
            Tour(cities=individual.cities, fitness_list=individual.fitness_list)
            for individual in individuals
        ]

    def get_problem_size(self) -> int:
        return len(self.nodes)

    def get_gene_space(self) -> List[int]:
        return list(range(len(self.nodes)))
