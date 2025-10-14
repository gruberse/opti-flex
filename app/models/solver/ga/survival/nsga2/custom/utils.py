from typing import List, Any, Generator

import numpy as np

from app.models.fitness.obj import Fitness
from app.models.individual.obj import Individual
from app.models.solver.ga.survival.nsga2.custom.individual import NSGA2Individual


def crowding_distances_assignment(individuals: List[NSGA2Individual]) -> List[NSGA2Individual]:
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
                nsga2_individuals[p_idx].dominated_individuals.append(nsga2_individuals[q_idx])
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
            for q in p.dominated_individuals:
                q.domination_count -= 1

                # if the domination count of q equals 0, then q is on the next front
                if q.domination_count == 0:
                    q.rank = current_front_idx + 1
                    next_front.append(q)

        current_front = crowding_distances_assignment(current_front)

        yield current_front

        current_front_idx += 1
        current_front = next_front


def test():
    individual = Individual(
        encoding=[0, 1, 2, 3, 4],
        fitness_list=[
            Fitness(objective_id='Objective 1', actual_fitness=100, estimated_fitness=None),
            Fitness(objective_id='Objective 2', actual_fitness=100, estimated_fitness=100)
        ]
    )

    nsga2_individual = NSGA2Individual(encoding=individual.encoding, fitness_list=individual.fitness_list)

    assert individual == nsga2_individual.to_individual()

    individuals = [
        Individual(
            encoding=[0],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=120, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=200, estimated_fitness=60),
            ]
        ),
        Individual(
            encoding=[1],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=99, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=100, estimated_fitness=100),
            ]
        ),
        Individual(
            encoding=[2],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=80, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=120, estimated_fitness=20),
            ]
        ),
        Individual(
            encoding=[3],
            fitness_list=[
                Fitness(objective_id='Objective 1', actual_fitness=50, estimated_fitness=None),
                Fitness(objective_id='Objective 2', actual_fitness=120, estimated_fitness=120),
            ]
        ),
    ]

    nsga2_individuals = []
    generator_non_dominated_sorting = fast_non_dominated_sorting(individuals)
    while len(nsga2_individuals) < len(individuals):
        current_front = next(generator_non_dominated_sorting)
        nsga2_individuals.extend(current_front)

    assert nsga2_individuals[0].rank == 0
    assert nsga2_individuals[0].crowding_distance == np.inf
    assert nsga2_individuals[0].domination_count == 0
    assert len(nsga2_individuals[0].dominated_individuals) == 1

    assert nsga2_individuals[1].rank == 0
    assert nsga2_individuals[1].crowding_distance == ((120 - 50) / (120 - 50)) + ((120 - 60) / (120 - 60))
    assert nsga2_individuals[1].domination_count == 0
    assert len(nsga2_individuals[1].dominated_individuals) == 1

    assert nsga2_individuals[2].rank == 0
    assert nsga2_individuals[2].crowding_distance == np.inf
    assert nsga2_individuals[2].domination_count == 0
    assert len(nsga2_individuals[2].dominated_individuals) == 0

    assert nsga2_individuals[3].rank == 1
    assert nsga2_individuals[3].crowding_distance == np.inf
    assert nsga2_individuals[3].domination_count == 0
    assert len(nsga2_individuals[3].dominated_individuals) == 0

