from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.offspring.base import OffspringSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class OffspringSelection(OffspringSelectionBase, SurvivorSelection):

    def select_survivors(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring