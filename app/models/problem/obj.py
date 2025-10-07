import concurrent.futures
from abc import abstractmethod
from typing import List

from app.models.population.obj import Population
from .base import ProblemBase
from ..individual.obj import Individual
from ..objective.obj import Objective


class Problem(ProblemBase):
    objectives: List[Objective]

    def evaluate_individuals(self, individuals: List[Individual]) -> List[Individual]:
        fitness_dict_population = {objective.objective_id: [] for objective in self.objectives}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(objective.get_evaluation_result, individuals): objective for objective in self.objectives}

            # Once the future is completed, the fitness is stored in the dictionary with the objective_id as the key
            for future in concurrent.futures.as_completed(futures):
                objective = futures[future]
                fitness_dict_population[objective.objective_id] = future.result()

        # assign the fitness objects to the population for each individual
        for i, individual in enumerate(individuals):
            individual.fitness_list = [fitness_dict_population[objective.objective_id][i] for objective in self.objectives]

        return individuals

    def evaluate_individual(self, individual: Individual) -> Individual:
        individual.fitness_list = [objective.get_fitness(encoding=individual.encoding) for objective in self.objectives]
        return individual

    @abstractmethod
    def update_result(self, individuals: List[Individual]) -> None:
        pass

    @abstractmethod
    def get_problem_size(self) -> int:
        pass

    @abstractmethod
    def get_gene_space(self) -> List[int]:
        pass
