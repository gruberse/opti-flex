import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.solver.ga.modification.inject_elitists.base import InjectElitistsModificationBase
from app.models.solver.ga.modification.obj import Modification


class InjectElitistsModification(InjectElitistsModificationBase, Modification):
    def modify_population(self, parents: List[Individual], offspring: List[Individual]) -> List[Individual]:
        temp_population = Population(population_id=-1, individuals=parents)
        elitists = temp_population.get_non_dominated_individuals()

        indices = sorted(random.sample(range(len(offspring)), len(elitists)))

        for i, idx in enumerate(indices):
            offspring[idx] = elitists[i]

        return offspring


def test():
    m = InjectElitistsModification()

    parents = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id='test', actual_fitness=100)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id='test', actual_fitness=90)]),
    ]
    offspring = [Individual(encoding=[2]), Individual(encoding=[3])]

    random.seed(1)

    individuals = m.modify_population(parents, offspring)

    assert len(individuals) == 2
    assert individuals[0].encoding == [0]
    assert individuals[1].encoding == [3]
