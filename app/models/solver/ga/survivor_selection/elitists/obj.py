from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.elitists.base import ElitistsSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class ElitistsSelection(ElitistsSelectionBase, SurvivorSelection):

    def select_survivors(self, individuals: List[Individual], population_size: int) -> List[Individual]:

        if 1 < len(individuals[0].fitness_list):
            raise RuntimeError('elitists selection can only be used for single-objective optimization')

        individuals.sort(key=lambda individual: individual.fitness_list[0].get_estimated_or_actual_fitness(), reverse=True)
        return individuals[:population_size]


def test():
    s = ElitistsSelection()
    population_size = 2

    individuals = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=50)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[2], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
        Individual(encoding=[3], fitness_list=[Fitness(objective_id='test', actual_fitness=100, estimated_fitness=60)]),
    ]

    survivors = s.select_survivors(individuals, population_size)

    assert survivors[0].encoding == [1]
    assert survivors[1].encoding == [2]
