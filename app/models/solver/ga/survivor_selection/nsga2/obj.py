from typing import List, Optional, Any, Generator

import numpy as np

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.custom.nsga2 import NSGA2Individual, NonDominatedSortingGeneticAlgorithmII
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2SurvivalSelectionBase

from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class NSGA2SurvivalSelection(NSGA2SurvivalSelectionBase, SurvivorSelection):

    def select_survivors(self, individuals: List[Individual], population_size: int) -> List[NSGA2Individual]:

        if len(individuals[0].fitness_list) < 2:
            raise RuntimeError('nsga2 survival selection can only be used for multi-objective optimization')

        survivors: List[NSGA2Individual] = []

        generator_non_dominated_sorting = NonDominatedSortingGeneticAlgorithmII.fast_non_dominated_sorting(individuals)

        while len(survivors) < population_size:
            current_front = next(generator_non_dominated_sorting)

            if len(survivors) + len(current_front) <= population_size:
                survivors.extend(current_front)

            else:
                # select the best solutions based on the crowding distance
                current_front.sort(key=lambda individual: individual.crowding_distance, reverse=True)
                n_remaining_individuals = population_size - len(survivors)
                survivors.extend(current_front[:n_remaining_individuals])

        return survivors


def test():
    s = NSGA2SurvivalSelection()

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

    survivors = s.select_survivors(individuals, 2)

    assert survivors[0].encoding == individuals[0].encoding
    assert survivors[1].encoding == individuals[3].encoding
