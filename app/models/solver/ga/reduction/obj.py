from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.reduction.base import ReductionBase


class Reduction(ReductionBase):
    @abstractmethod
    def reduce_individuals(self, individuals: List[Individual], n_individuals: int) -> List[Individual]:
        pass