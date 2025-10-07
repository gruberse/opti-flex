from typing import List

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation
from app.models.solver.ga.fitness_evaluation.offspring.base import OffspringEvaluationBase


class OffspringEvaluation(OffspringEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return problem.evaluate_individuals(offspring)