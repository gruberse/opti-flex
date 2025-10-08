from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.modification.base import ModificationBase


class Modification(ModificationBase):
    @abstractmethod
    def modify_population(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        pass