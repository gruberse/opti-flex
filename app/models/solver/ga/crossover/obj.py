from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.crossover.base import CrossoverBase


class Crossover(CrossoverBase):
    @abstractmethod
    def crossover_parents(self, parents: List[Individual], population_size: int) -> List[Individual]:
        pass
