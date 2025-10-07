from typing import List

import numpy as np
from numpy.matrixlib.defmatrix import matrix

from app.models.individual.obj import Individual
from app.models.objective.obj import Objective
from app.models.objective.tsp.obj import TravelingSalesmanProblemObjective
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.problem.tsp.obj import TravelingSalesmanProblem
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation
from app.models.solver.ga.fitness_evaluation.offspring.base import OffspringEvaluationBase


class OffspringEvaluation(OffspringEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return problem.evaluate_individuals(offspring)


def test():
    e = OffspringEvaluation()

    problem = TravelingSalesmanProblem(
        objectives=[
            TravelingSalesmanProblemObjective(objective_id="test", matrix=np.array([
                [0, 1, 2],
                [3, 0, 4],
                [5, 6, 0]
            ]))
        ]
    )

    parents = [
        Individual(encoding=[0, 1, 2])
    ]

    offspring = [
        Individual(encoding=[2, 1, 0])
    ]

    evaluated_individuals = e.evaluate_individuals(problem, parents, offspring)

    assert len(evaluated_individuals) == 1
    assert evaluated_individuals[0].encoding == [2, 1, 0]
