from typing import List, Any

from app.models.individual.obj import Individual
from app.models.solver.ga.re_evaluation.none.base import NoReEvaluationBase
from app.models.solver.ga.re_evaluation.obj import ReEvaluation


class NoReEvaluation(NoReEvaluationBase, ReEvaluation):
    def get_remaining_population_size(self, population_size: int) -> int:
        return population_size

    def get_evaluation_individuals(self, parents: List[Individual], offspring: List[Individual],
                                   survival_selection: Any) -> List[Individual]:
        return offspring