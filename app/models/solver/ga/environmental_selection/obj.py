from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.environmental_selection.base import EnvironmentalSelectionBase


class EnvironmentalSelection(EnvironmentalSelectionBase):
    @abstractmethod
    def select_individuals(self, individuals: List[Individual], n_individuals: int) -> List[Individual]:
        pass