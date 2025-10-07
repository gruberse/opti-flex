from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.objective.tsp.obj import TravelingSalesmanProblemObjective
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.problem.tsp.obj import TravelingSalesmanProblem
from app.models.solver.ga.fitness_evaluation.combined.base import CombinedEvaluationBase
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation


class CombinedEvaluation(CombinedEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return problem.evaluate_individuals(parents + offspring)

def test():
    e = CombinedEvaluation()

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

    assert len(evaluated_individuals) == 2
    assert evaluated_individuals[0].encoding == [0, 1, 2]
    assert evaluated_individuals[1].encoding == [2, 1, 0]