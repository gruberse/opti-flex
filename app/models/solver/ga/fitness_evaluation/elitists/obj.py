import random
from typing import List

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.fitness_evaluation.elitists.base import ElitistsEvaluationBase
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation


class ElitistsEvaluation(ElitistsEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        individuals = offspring

        temp = Population(population_id=-1, individuals=parents)
        non_dominated_individuals = temp.get_non_dominated_individuals()

        if self.replace_offspring:
            replacement_indices = sorted(random.sample(range(len(offspring)), len(non_dominated_individuals)))

            for i, index in enumerate(replacement_indices):
                individuals[index] = non_dominated_individuals[i]
        else:
            individuals = individuals + non_dominated_individuals

        return problem.evaluate_individuals(individuals)