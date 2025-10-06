from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.elitists.base import ElitistsSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class ElitistsSelection(ElitistsSelectionBase, SurvivorSelection):
    def select_survivors(self, population_size: int, individuals: List[Individual]) -> List[Individual]:
        individuals.sort(key=lambda individual: individual.fitness_list[0].get_estimated_or_actual_fitness(), reverse=True)
        return individuals[:population_size]