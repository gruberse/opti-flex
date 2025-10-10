from typing import List

from app.models.individual.obj import Individual

from app.models.solver.ga.re_evaluation.dto import ReEvaluationDTO
from app.models.solver.ga.re_evaluation.obj import ReEvaluation
from app.models.solver.ga.re_evaluation.population.base import PopulationReEvaluationBase


class PopulationReEvaluation(PopulationReEvaluationBase, ReEvaluation):

    def select_individuals(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return parents + offspring


def test():
    m = PopulationReEvaluation()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.select_individuals(parents, offspring)

    assert len(individuals) == 2

    assert individuals[0].encoding == [0]
    assert individuals[1].encoding == [1]
