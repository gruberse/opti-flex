from typing import List, Any

from app.models.individual.obj import Individual

from app.models.solver.ga.re_evaluation.elitists.base import ElitistsReEvaluationBase
from app.models.solver.ga.re_evaluation.obj import ReEvaluation


class ElitistsReEvaluation(ElitistsReEvaluationBase, ReEvaluation):

    def get_remaining_population_size(self, population_size: int) -> int:
        return population_size - self.n_elitists

    def select_individuals(self, parents: List[Individual], offspring: List[Individual], survival_selection: Any) -> List[Individual]:
        elitists = survival_selection.select_individuals(parents, self.n_elitists)
        return elitists + offspring


def test():
    m = ElitistsReEvaluation()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.select_individuals(parents, offspring)

    assert len(individuals) == 1
    assert individuals[0].encoding == [1]