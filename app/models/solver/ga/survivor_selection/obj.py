from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.survivor_selection.base import SurvivorSelectionBase


class SurvivorSelection(SurvivorSelectionBase):
    @abstractmethod
    def select_individuals(self, individuals: List[Individual], n_survivors: int) -> List[Individual]:
        pass