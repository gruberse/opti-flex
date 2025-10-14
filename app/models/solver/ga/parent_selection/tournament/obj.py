import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.parent_selection.tournament.base import TournamentSelectionBase


class TournamentSelection(TournamentSelectionBase, ParentSelection):

    def select_individuals(self, individuals: List[Individual], n_parents: int) -> List[Individual]:

        if 1 < len(individuals[0].fitness_list):
            raise RuntimeError('tournament selection can only be used for single-objective optimization')

        parent_individuals = []

        for _ in range(n_parents):
            participant_indices = random.sample(range(len(individuals)), self.tournament_size)

            # select the participant individuals
            participant_individuals = [individuals[i] for i in participant_indices]

            # identify the max fitness of the participants
            max_fitness = max([
                individual.fitness_list[0].get_estimated_or_actual_fitness()
                for individual in participant_individuals
            ])

            # identify the individuals of the participants with the max fitness
            best_participant_individuals = [
                individual for individual in participant_individuals
                if individual.fitness_list[0].get_estimated_or_actual_fitness() == max_fitness
            ]

            # randomly select one of the best participant individuals
            selected_individual = random.choice(best_participant_individuals)

            parent_individuals.append(selected_individual)

        return parent_individuals


def test():
    s = TournamentSelection(tournament_size=2)

    individuals = [
        Individual(encoding=[0], fitness_list=[Fitness(objective_id='test', actual_fitness=100)]),
        Individual(encoding=[1], fitness_list=[Fitness(objective_id='test', actual_fitness=90)]),
        Individual(encoding=[2], fitness_list=[Fitness(objective_id='test', actual_fitness=80)]),
        Individual(encoding=[3], fitness_list=[Fitness(objective_id='test', actual_fitness=70)]),
        Individual(encoding=[4], fitness_list=[Fitness(objective_id='test', actual_fitness=90)]),
        Individual(encoding=[5], fitness_list=[Fitness(objective_id='test', actual_fitness=50)]),
    ]

    random.seed(1)

    parents = s.select_individuals(individuals, 2)

    assert parents[0] == individuals[1]
    assert parents[1] == individuals[0]