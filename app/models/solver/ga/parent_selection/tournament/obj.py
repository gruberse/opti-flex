import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.parent_selection.tournament.base import TournamentSelectionBase


class TournamentSelection(TournamentSelectionBase, ParentSelection):
    def select_parents(self, individuals: List[Individual]) -> List[Individual]:
        parent_individuals = []
        population_size = len(individuals)

        for _ in range(population_size):
            participant_indices = random.sample(range(population_size), self.tournament_size)

            # select the participant individuals
            participant_individuals = [individuals[i] for i in participant_indices]

            # identify the max fitness of the participants
            max_fitness = max([
                individual.fitness_list[0].get_estimated_or_actual_fitness()
                for individual in participant_individuals
            ])

            # identify the individuals of the participants with the max fitness
            best_participant_individuals = [
                solution for solution in participant_individuals
                if solution.fitness_list[0].get_estimated_or_actual_fitness() == max_fitness
            ]

            # randomly select one of the best participant individuals
            selected_individual = random.choice(best_participant_individuals)

            parent_individuals.append(selected_individual)

        return parent_individuals


def test():
    ts = TournamentSelection(tournament_size=6)

    individuals = [
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=100)]),
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=90)]),
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=80)]),
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=70)]),
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=60)]),
        Individual(encoding=[], fitness_list=[Fitness(objective_id='test', actual_fitness=50)]),
    ]

    parents = ts.select_parents(individuals)
    for parent in parents:
        assert parent == individuals[0]