import random
from typing import List

from app.models.individual.obj import Individual
from app.models.solver.ga.parent_selection.nsga2.base import NSGA2ParentSelectionBase
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2Individual


class NSGA2ParentSelection(NSGA2ParentSelectionBase, ParentSelection):
    def select_parents(self, individuals: List[NSGA2Individual]) -> List[Individual]:
        parent_individuals = []
        population_size = len(individuals)

        for _ in range(population_size):
            participant_indices = random.sample(range(population_size), self.tournament_size)

            # select the participant individuals
            participant_individuals = [individuals[i] for i in participant_indices]

            # identify the min rank of the participants
            min_rank = min([individual.rank for individual in participant_individuals])

            # identify the individuals of the participants with the min rank
            best_participant_individuals = [
                individual for individual in participant_individuals
                if individual.rank == min_rank
            ]

            if len(best_participant_individuals) > 1:
                # identify the max crowding distance of the best individuals
                max_crowding_distance = max(
                    individual.crowding_distance for individual in best_participant_individuals)

                # identify the individuals of the best individuals with the max crowding distance
                best_participant_individuals = [
                    individual for individual in best_participant_individuals
                    if individual.crowding_distance == max_crowding_distance
                ]

            # randomly select one of the best participant individuals
            selected_individual = random.choice(best_participant_individuals)

            parent_individuals.append(selected_individual.to_individual())

        return parent_individuals
