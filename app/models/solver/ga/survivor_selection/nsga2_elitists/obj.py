from typing import List, Optional, Any, Generator

import numpy as np

from app.models.individual.obj import Individual

from app.models.solver.ga.survivor_selection.nsga2_elitists.base import NSGA2basedElitistsSelectionBase
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection


class NSGA2Individual(Individual):
    domination_count: int = 0
    dominated_solutions: List = []
    rank: Optional[int] = None
    crowding_distance: float = 0.0

    def to_individual(self) -> Individual:
        return Individual(
            encoding=self.encoding,
            fitness_list=self.fitness_list,
        )


def calculate_crowding_distances(individuals: List[NSGA2Individual]) -> List[NSGA2Individual]:
    for i in range(len(individuals[0].fitness_list)):
        fitness_values = np.array(
            [individual.fitness_list[i].get_estimated_or_actual_fitness() for individual in individuals]
        )

        min_fitness = np.min(fitness_values)
        max_fitness = np.max(fitness_values)

        indices = np.argsort(fitness_values)

        individuals[indices[0]].crowding_distance = np.inf
        individuals[indices[-1]].crowding_distance = np.inf

        for j in range(1, len(individuals) - 1):
            prev_fitness = fitness_values[indices[j - 1]]
            next_fitness = fitness_values[indices[j + 1]]

            if max_fitness != min_fitness:
                individuals[indices[j]].crowding_distance += (next_fitness - prev_fitness) / (
                        max_fitness - min_fitness)

    return individuals


def fast_non_dominated_sorting(individuals: List[Individual]) -> Generator[list[NSGA2Individual], Any, None]:
    nsga2_individuals = []

    for individual in individuals:
        nsga2_individuals.append(
            NSGA2Individual(
                encoding=individual.encoding,
                fitness_list=individual.fitness_list,
            )
        )

    fitness_arrays = [
        np.array([
            fitness.get_estimated_or_actual_fitness()
            for fitness in individual.fitness_list
        ])
        for individual in individuals
    ]

    current_front = []

    for p_idx, p_fitness_array in enumerate(fitness_arrays):
        for q_idx, q_fitness_array in enumerate(fitness_arrays):
            if p_idx == q_idx:
                continue

            # if p strictly dominates q, add q to the dominated solutions
            if np.all(p_fitness_array >= q_fitness_array) and np.any(p_fitness_array > q_fitness_array):
                nsga2_individuals[p_idx].dominated_solutions.append(nsga2_individuals[q_idx])
            # if p is strictly dominated by q, increase the domination count
            elif np.all(q_fitness_array >= p_fitness_array) and np.any(q_fitness_array > p_fitness_array):
                nsga2_individuals[p_idx].domination_count += 1

        # if p is on the best front
        if nsga2_individuals[p_idx].domination_count == 0:
            nsga2_individuals[p_idx].rank = 0
            current_front.append(nsga2_individuals[p_idx])


    # retrieve the remaining fronts
    current_front_idx = 0
    while current_front:
        next_front = []

        for p in current_front:
            # reduce the domination count of dominated solutions
            for q in p.dominated_solutions:
                q.domination_count -= 1

                # if the domination count of q equals 0, then q is on the next front
                if q.domination_count == 0:
                    q.rank = current_front_idx + 1
                    next_front.append(q)

        current_front = calculate_crowding_distances(current_front)

        yield current_front

        current_front_idx += 1
        current_front = next_front



class NSGA2BasedElitistsSelection(NSGA2basedElitistsSelectionBase, SurvivorSelection):

    def select_survivors(self, population_size: int, individuals: List[Individual]) -> List[NSGA2Individual]:
        survivors: List[NSGA2Individual] = []

        generator_non_dominated_sorting = fast_non_dominated_sorting(individuals)

        while len(survivors) < population_size:
            current_front = next(generator_non_dominated_sorting)

            if len(survivors) + len(current_front) <= population_size:
                survivors.extend(current_front)

            else:
                # select the best solutions based on the crowding distance
                current_front.sort(key=lambda individual: individual.crowding_distance, reverse=True)
                n_remaining_individuals = population_size - len(survivors)
                survivors.extend(current_front[:n_remaining_individuals])

        return survivors
