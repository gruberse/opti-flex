from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.evaluation_mode.comma.base import CommaModeBase
from app.models.solver.ga.evaluation_mode.obj import EvaluationMode


class CommaMode(CommaModeBase, EvaluationMode):

    def select_individuals(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring


def test():
    m = CommaMode()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.select_individuals(parents, offspring)

    assert len(individuals) == 1
    assert individuals[0].encoding == [1]