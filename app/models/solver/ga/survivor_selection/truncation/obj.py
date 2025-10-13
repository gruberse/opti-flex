import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection
from app.models.solver.ga.survivor_selection.truncation.base import TruncationSelectionBase


class TruncationSelection(TruncationSelectionBase, SurvivorSelection):

    def select_individuals(self, individuals: List[Individual], n_survivors: int) -> List[Individual]:

        if 1 < len(individuals[0].fitness_list):
            raise RuntimeError('top k parent_selection can only be used for single-objective optimization')

        if len(individuals) <= n_survivors:
            return individuals

        # shuffle in case of many individuals having the same fitness
        random.shuffle(individuals)

        individuals.sort(key=lambda individual: individual.fitness_list[0].get_estimated_or_actual_fitness(), reverse=True)
        return individuals[:n_survivors]


def test():
    s = TruncationSelection()
    population_size = 2

    individuals = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=50)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[2], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[3], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
    ]

    random.seed(1)

    survivors = s.select_individuals(individuals, population_size)

    assert survivors[0].encoding == [3]
    assert survivors[1].encoding == [2]
