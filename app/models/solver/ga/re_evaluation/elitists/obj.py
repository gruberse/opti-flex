from typing import List

from app.models.individual.obj import Individual

from app.models.solver.ga.re_evaluation.elitists.base import ElitistsReEvaluationBase
from app.models.solver.ga.re_evaluation.obj import ReEvaluation


class ElitistsReEvaluation(ElitistsReEvaluationBase, ReEvaluation):

    def select_individuals(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring


def test():
    m = ElitistsReEvaluation()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.select_individuals(parents, offspring)

    assert len(individuals) == 1
    assert individuals[0].encoding == [1]