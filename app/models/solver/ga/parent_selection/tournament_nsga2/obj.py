import random
from typing import List

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.parent_selection.tournament_nsga2.base import NSGA2basedTournamentSelectionBase
from app.models.solver.ga.survivor_selection.nsga2.custom.individual import NSGA2Individual


class NSGA2BasedTournamentSelection(NSGA2basedTournamentSelectionBase, ParentSelection):

    def select_parents(self, individuals: List[NSGA2Individual], n_parents: int) -> List[Individual]:

        if len(individuals[0].fitness_list) < 2:
            raise RuntimeError('nsga2 based tournament selection can only be used for multi-objective optimization')

        if not isinstance(individuals[0], NSGA2Individual):
            raise RuntimeError('nsga2 based tournament selection can only be used together with nsga2 based survivor selection')

        parent_individuals = []

        for _ in range(n_parents):
            participant_indices = random.sample(range(len(individuals)), self.tournament_size)

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

def test():
    s = NSGA2BasedTournamentSelection(tournament_size=2)

    individuals = [
        NSGA2Individual(encoding=[0], fitness_list=[
            Fitness(objective_id='Objective 1', actual_fitness=100, estimated_fitness=100),
            Fitness(objective_id='Objective 2', actual_fitness=100, estimated_fitness=100),
        ], rank=1, crowding_distance=1.0),
        NSGA2Individual(encoding=[1], fitness_list=[], rank=2, crowding_distance=0.5),
        NSGA2Individual(encoding=[2], fitness_list=[], rank=1, crowding_distance=1.0),
        NSGA2Individual(encoding=[3], fitness_list=[], rank=3, crowding_distance=0.5),
        NSGA2Individual(encoding=[4], fitness_list=[], rank=2, crowding_distance=1.0),
        NSGA2Individual(encoding=[5], fitness_list=[], rank=4, crowding_distance=1.0),
    ]

    random.seed(1)

    parents = s.select_parents(individuals, 3)

    assert parents[0] == individuals[4].to_individual()
    assert parents[1] == individuals[0].to_individual()
    assert parents[2] == individuals[3].to_individual()

    assert isinstance(parents[0], NSGA2Individual) == False
    assert isinstance(parents[1], NSGA2Individual) == False
    assert isinstance(parents[2], NSGA2Individual) == False