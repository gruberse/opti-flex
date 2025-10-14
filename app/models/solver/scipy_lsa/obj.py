import concurrent.futures
import multiprocessing
from datetime import datetime
from typing import List, Optional, Dict

import numpy as np
from scipy.optimize import linear_sum_assignment

from app.models.population.obj import Population
from .base import ScipyLinearSumAssignmentBase
from .weight.obj import Weight
from .weights.obj import Weights
from ..obj import Solver
from ...individual.obj import Individual
from ...problem.ap.obj import AssignmentProblem


class ScipyLinearSumAssignment(ScipyLinearSumAssignmentBase, Solver):
    weights_list: Optional[List[Weights]] = None

    @staticmethod
    def _solve(weights: Weights, normalized_matrices: Dict, problem: AssignmentProblem, maximize: bool) -> Individual:
        # combine objective_weight matrix for given weights
        combined_weight_matrix = np.zeros_like(normalized_matrices.get(list(normalized_matrices.keys())[0]))

        for weight in weights.weight_list:
            combined_weight_matrix += weight.value * normalized_matrices[weight.objective_id]

        # compute an optimal solution
        row_ind, col_ind = linear_sum_assignment(cost_matrix=combined_weight_matrix, maximize=maximize)

        # not every flight may have a tta assigned and vice versa
        encoding: np.ndarray = np.full(problem.get_problem_size(), -1, dtype=int)
        for i in range(len(row_ind)):
            encoding[row_ind[i]] = col_ind[i]

        # evaluate and return solution
        return problem.evaluate_individual(Individual(encoding=encoding.tolist()))

    def solve(self, problem: AssignmentProblem, population_queue: multiprocessing.Queue, populations: List[Population]) -> None:
        for objective in problem.objectives:
            if objective.privacy_engine or objective.obfuscation:
                raise RuntimeError("ScipyFramework does not support privacy engine or obfuscation")

        # normalize matrices of objectives (if available) based on true min and max values
        normalized_matrices: dict = {}
        for objective in problem.objectives:
            min_value = np.min(objective.matrix)
            max_value = np.max(objective.matrix)

            if max_value != min_value:
                # normalize matrix based on true min and max values
                normalized_matrices[objective.objective_id] = (objective.matrix - min_value) / (
                        max_value - min_value)
            else:
                # if all values are equal, set them to 1
                normalized_matrices[objective.objective_id] = np.ones_like(objective.matrix)

        # if no weightings are provided, use the same weight for each objective
        weights_list = self.weights_list
        if weights_list is None or len(weights_list) == 0:
            weights = Weights(weight_list=[])
            value = 1.0 / len(problem.objectives)
            for objective in problem.objectives:
                weights.weight_list.append(
                    Weight(objective_id=objective.objective_id, value=value))
            weights_list = [weights]

        # only 1 population object with scipy
        population = Population(population_id=0, start_time=datetime.now())

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(ScipyLinearSumAssignment._solve, weights, normalized_matrices, problem, self.maximize):
                           weights for weights in weights_list}

            for future in concurrent.futures.as_completed(futures):
                population.individuals.append(future.result())

        population.end_time = datetime.now()

        populations.append(population)

        population_queue.put(population.population_id)

        # stop the population process
        population_queue.put(None)
