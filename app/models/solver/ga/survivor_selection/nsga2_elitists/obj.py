from typing import List, Optional, Any, Generator

import numpy as np

from app.models.individual.obj import Individual
from app.models.solver.ga.custom.nsga2 import NSGA2Individual, NSGA2

from app.models.solver.ga.survivor_selection.nsga2_elitists.base import NSGA2basedElitistsSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class NSGA2BasedElitistsSelection(NSGA2basedElitistsSelectionBase, SurvivorSelection):

    def select_survivors(self, population_size: int, individuals: List[Individual]) -> List[NSGA2Individual]:
        survivors: List[NSGA2Individual] = []

        generator_non_dominated_sorting = NSGA2.fast_non_dominated_sorting(individuals)

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
