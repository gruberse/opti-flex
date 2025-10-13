from typing import List, Optional, Any, Generator

import numpy as np

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2basedSurvivorSelectionBase
from app.models.solver.ga.survivor_selection.nsga2.custom.individual import NSGA2Individual
from app.models.solver.ga.survivor_selection.nsga2.custom.utils import fast_non_dominated_sorting

from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class NSGA2basedSurvivorSelection(NSGA2basedSurvivorSelectionBase, SurvivorSelection):

    def select_individuals(self, individuals: List[Individual], n_survivors: int) -> List[NSGA2Individual]:

        if len(individuals[0].fitness_list) < 2:
            raise RuntimeError('nsga2 survivor_selection can only be used for multi-objective optimization')

        survivors: List[NSGA2Individual] = []

        generator_non_dominated_sorting = fast_non_dominated_sorting(individuals)

        while len(survivors) < n_survivors:
            current_front = next(generator_non_dominated_sorting)

            if len(survivors) + len(current_front) <= n_survivors:
                survivors.extend(current_front)

            else:
                # select the best solutions based on the crowding distance
                current_front.sort(key=lambda individual: individual.crowding_distance, reverse=True)
                n_remaining_individuals = n_survivors - len(survivors)
                survivors.extend(current_front[:n_remaining_individuals])

        return survivors


def test():
    s = NSGA2basedSurvivorSelection()

    individuals = [
        Individual(
            encoding=[0],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=120, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=200, estimated_fitness=60),
            ]
        ),
        Individual(
            encoding=[1],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=99, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=100, estimated_fitness=100),
            ]
        ),
        Individual(
            encoding=[2],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=80, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=120, estimated_fitness=20),
            ]
        ),
        Individual(
            encoding=[3],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=50, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=120, estimated_fitness=120),
            ]
        ),
    ]

    survivors = s.select_individuals(individuals, 2)

    assert survivors[0].encoding == individuals[0].encoding
    assert survivors[1].encoding == individuals[3].encoding
