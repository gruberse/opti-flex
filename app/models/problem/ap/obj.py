from typing import List

from .assignment.obj import Assignment
from .base import AssignmentProblemBase
from ..obj import Problem
from ...individual.obj import Individual
from ...objective.ap.obj import AssignmentObjective


class AssignmentProblem(AssignmentProblemBase, Problem):
    objectives: List[AssignmentObjective] = []
    result_assignments: List[Assignment] = []

    def __init__(self, /, **data):
        super().__init__(**data)
        for objective in self.objectives:
            objective.init_evaluation_setup()

    def get_problem_size(self) -> int:
        return max(self.objectives[0].matrix.shape)

    def get_gene_space(self) -> List[int]:
        gene_space = list(range(min(self.objectives[0].matrix.shape)))

        diff = abs(self.objectives[0].matrix.shape[0] - self.objectives[0].matrix.shape[1])
        if diff > 0:
            for i in range(diff):
                gene_space.append(-1 - i)

        return gene_space

    def update_result(self, individuals: List[Individual]) -> None:
        temp_results = []

        for individual in individuals:
            assignments = []

            for row_idx, col_idx in enumerate(individual.encoding):
                if self.objectives[0].transposed:
                    row_idx, col_idx = col_idx, row_idx

                if row_idx > -1 and col_idx > -1:
                    assignments.append((row_idx, col_idx))

            assignments.sort(key=lambda x: x[0])  # Sort by row index

            temp_results.append(Assignment(
                row_ind=[assignment[0] for assignment in assignments],
                col_ind=[assignment[1] for assignment in assignments],
                fitness_list=individual.fitness_list
            ))

        self.result_assignments = temp_results