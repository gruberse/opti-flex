import random
from typing import List

import numpy as np

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.objective.tsp.obj import TravelingSalesmanObjective
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.problem.tsp.obj import TravelingSalesmanProblem
from app.models.solver.ga.fitness_evaluation.elitists.base import ElitistsEvaluationBase
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation


class ElitistsEvaluation(ElitistsEvaluationBase, FitnessEvaluation):
    def evaluate_individuals(self, problem: Problem, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        individuals = offspring.copy()

        temp = Population(population_id=-1, individuals=parents)
        non_dominated_individuals = temp.get_non_dominated_individuals()

        if self.replace_offspring:
            replacement_indices = sorted(random.sample(range(len(offspring)), len(non_dominated_individuals)))

            for i, index in enumerate(replacement_indices):
                individuals[index] = non_dominated_individuals[i]
        else:
            individuals = individuals + non_dominated_individuals

        return problem.evaluate_individuals(individuals)


def test():
    e = ElitistsEvaluation(replace_offspring=False)

    problem = TravelingSalesmanProblem(
        objectives=[
            TravelingSalesmanObjective(objective_id="test", matrix=np.array([
                [0, 1, 2],
                [3, 0, 4],
                [5, 6, 0]
            ]))
        ]
    )

    parents = [
        Individual(encoding=[0, 1, 2], fitness_list=[Fitness(objective_id='test', actual_fitness=100)]),
        Individual(encoding=[1, 2, 0], fitness_list=[Fitness(objective_id='test', actual_fitness=50)])
    ]

    offspring = [
        Individual(encoding=[2, 1, 0]),
        Individual(encoding=[0, 2, 1])
    ]

    random.seed(1)

    evaluated_individuals = e.evaluate_individuals(problem, parents, offspring)

    assert len(evaluated_individuals) == 3
    assert evaluated_individuals[0].encoding == [2, 1, 0]
    assert evaluated_individuals[1].encoding == [0, 2, 1]
    assert evaluated_individuals[2].encoding == [0, 1, 2]

    e = ElitistsEvaluation(replace_offspring=True)

    evaluated_individuals = e.evaluate_individuals(problem, parents, offspring)

    assert len(evaluated_individuals) == 2
    assert evaluated_individuals[0].encoding == [0, 1, 2]
    assert evaluated_individuals[1].encoding == [0, 2, 1]
