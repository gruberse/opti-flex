from abc import abstractmethod
from typing import List, Any

from app.models.individual.obj import Individual
from app.models.solver.ga.re_evaluation.base import ReEvaluationBase


class ReEvaluation(ReEvaluationBase):

    @abstractmethod
    def get_remaining_population_size(self, population_size: int) -> int:
        pass

    @abstractmethod
    def select_individuals(self, parents: List[Individual], offspring: List[Individual], survival_selection: Any) -> List[Individual]:
        pass