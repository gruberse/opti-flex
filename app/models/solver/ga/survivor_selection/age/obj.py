from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.age.base import AgeBasedSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class AgeBasedSelection(AgeBasedSelectionBase, SurvivorSelection):

    def select_survivors(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring