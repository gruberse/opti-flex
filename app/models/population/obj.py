from typing import List

import numpy as np

from app.models.fitness.obj import Fitness
from .base import PopulationBase
from ..individual.obj import Individual


class Population(PopulationBase):
    individuals: List[Individual] = []
    non_dominated_individuals: List[Individual] = []

    def _get_unique_individuals(self) -> List[Individual]:
        individual_groups: dict = {}
        for individual in self.individuals:
            # set all negative placeholder values to None
            modified_encoding = np.where(np.array(individual.encoding) < 0, None, individual.encoding)
            encoding_tuple = tuple(modified_encoding)

            if individual_groups.get(encoding_tuple) is None:
                individual_groups[encoding_tuple] = []

            individual_groups[encoding_tuple].append(individual)

        unique_individuals: List[Individual] = []

        # if there are duplicate solutions, choose the maximum fitness of each objective
        for encoding, individuals in individual_groups.items():
            fitness_dict: dict[str, Fitness] = {}
            for individual in individuals:
                for fitness in individual.fitness_list:
                    if fitness_dict.get(fitness.objective_id) is None:
                        fitness_dict[fitness.objective_id] = Fitness(
                            objective_id=fitness.objective_id,
                            actual_fitness=fitness.actual_fitness,
                            estimated_fitness=fitness.estimated_fitness)
                    else:
                        if (fitness_dict[fitness.objective_id].actual_fitness is None
                                or fitness.actual_fitness > fitness_dict[fitness.objective_id].actual_fitness):
                            fitness_dict[fitness.objective_id].actual_fitness = fitness.actual_fitness

                        if (fitness_dict[fitness.objective_id].estimated_fitness is None
                                or fitness.estimated_fitness > fitness_dict[fitness.objective_id].estimated_fitness):
                            fitness_dict[fitness.objective_id].estimated_fitness = fitness.estimated_fitness

            modified_encoding = np.where(np.array(encoding) == None, -1, encoding).tolist()
            unique_individual = Individual(encoding=modified_encoding, fitness_list=list(fitness_dict.values()))
            unique_individuals.append(unique_individual)

        return unique_individuals

    def get_non_dominated_individuals(self) -> List[Individual]:
        individuals: List[Individual] = []
        unique_individuals = self._get_unique_individuals()

        fitness_arrays = [
            np.array([
                fitness.get_estimated_or_actual_fitness()
                for fitness in individual.fitness_list
            ])
            for individual in unique_individuals
        ]

        for i, i_fitness_array in enumerate(fitness_arrays):
            is_non_dominated = True

            for j, j_fitness_array in enumerate(fitness_arrays):
                if i == j:
                    continue

                if np.all(i_fitness_array <= j_fitness_array) and np.any(i_fitness_array < j_fitness_array):
                    is_non_dominated = False
                    break

            if is_non_dominated:
                individuals.append(unique_individuals[i])

        return individuals
