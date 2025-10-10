from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.parent_selection.base import ParentSelectionBase


class ParentSelection(ParentSelectionBase):
    @abstractmethod
    def select_individuals(self, individuals: List[Individual], n_parents: int) -> List[Individual]:
        pass
