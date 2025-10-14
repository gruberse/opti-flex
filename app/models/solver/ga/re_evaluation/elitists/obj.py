from typing import List, Any

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.re_evaluation.elitists.base import ElitistsReEvaluationBase
from app.models.solver.ga.re_evaluation.obj import ReEvaluation
from app.models.solver.ga.environmental_selection.truncation.obj import TruncationSelection


class ElitistsReEvaluation(ElitistsReEvaluationBase, ReEvaluation):

    def get_remaining_population_size(self, population_size: int) -> int:
        return population_size - self.n_elitists

    def select_evaluation_individuals(self, parents: List[Individual], offspring: List[Individual], survival_selection: Any) -> List[Individual]:
        elitists = survival_selection.select_individuals(parents, self.n_elitists)
        return elitists + offspring


def test():
    m = ElitistsReEvaluation(n_elitists=1)

    parents = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id="test", actual_fitness=100)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id="test", actual_fitness=90)])
    ]
    offspring = [Individual(encoding=[2])]

    individuals = m.select_evaluation_individuals(parents, offspring, TruncationSelection())

    assert len(individuals) == 2
    assert individuals[0].encoding == [0]
    assert individuals[1].encoding == [2]
