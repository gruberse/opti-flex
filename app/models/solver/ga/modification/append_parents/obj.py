from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.modification.append_parents.base import AppendParentsModificationBase
from app.models.solver.ga.modification.obj import Modification


class AppendParentsModification(AppendParentsModificationBase, Modification):
    def modify_population(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring + parents

def test():
    m = AppendParentsModification()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.modify_population(parents, offspring)

    assert len(individuals) == 2
    assert individuals[0].encoding == [1]
    assert individuals[1].encoding == [0]
