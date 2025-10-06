from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.generational.base import GenerationalSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class GenerationalSelection(GenerationalSelectionBase, SurvivorSelection):

    def select_survivors(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring