from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.modification.none.base import NoneModificationBase
from app.models.solver.ga.modification.obj import Modification


class NoneModification(NoneModificationBase, Modification):
    def modify_population(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        return offspring

def test():
    m = NoneModification()

    parents = [Individual(encoding=[0])]
    offspring = [Individual(encoding=[1])]

    individuals = m.modify_population(parents, offspring)

    assert len(individuals) == 1
    assert individuals[0].encoding == [1]