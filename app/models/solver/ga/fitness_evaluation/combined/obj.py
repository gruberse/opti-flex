from typing import List

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.fitness_evaluation.combined.base import CombinedEvaluationBase
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation


class CombinedEvaluation(CombinedEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        combined_individuals = parents + offspring
        return problem.evaluate_individuals(combined_individuals)