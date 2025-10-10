from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.mutation.base import MutationBase


class Mutation(MutationBase):

    @abstractmethod
    def mutate_offspring(self, offspring: List[Individual]) -> List[Individual]:
        pass
