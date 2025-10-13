from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.selection.base import SelectionBase


class Selection(SelectionBase):
    @abstractmethod
    def select_parents(self, individuals: List[Individual], n_parents: int) -> List[Individual]:
        pass
