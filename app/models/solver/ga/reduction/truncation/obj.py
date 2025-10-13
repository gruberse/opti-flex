import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.reduction.obj import Reduction
from app.models.solver.ga.reduction.truncation.base import TruncationReductionBase


class TruncationReduction(TruncationReductionBase, Reduction):

    def reduce_individuals(self, individuals: List[Individual], n_individuals: int) -> List[Individual]:

        if 1 < len(individuals[0].fitness_list):
            raise RuntimeError('top k selection can only be used for single-objective optimization')

        if len(individuals) <= n_individuals:
            return individuals

        # shuffle in case of many individuals having the same fitness
        random.shuffle(individuals)

        individuals.sort(key=lambda individual: individual.fitness_list[0].get_estimated_or_actual_fitness(), reverse=True)
        return individuals[:n_individuals]


def test():
    s = TruncationReduction()
    population_size = 2

    individuals = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=50)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[2], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[3], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
    ]

    random.seed(1)

    survivors = s.reduce_individuals(individuals, population_size)

    assert survivors[0].encoding == [3]
    assert survivors[1].encoding == [2]
