from abc import abstractmethod
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.re_evaluation.base import ReEvaluationBase


class ReEvaluation(ReEvaluationBase):

    @abstractmethod
    def select_individuals(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        pass