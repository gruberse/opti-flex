from typing import List

from .base import AssignmentProblemBase
from .assignment.dto import AssignmentDTO
from ..dto import ProblemDTO
from ...objective.ap.dto import AssignmentProblemObjectiveDTO


class AssignmentProblemInputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentProblemObjectiveDTO]


class AssignmentProblemOutputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentProblemObjectiveDTO]
    result_assignments: List[AssignmentDTO] = []


class AssignmentProblemOutputResultDTO(AssignmentProblemBase, ProblemDTO):
    result_assignments: List[AssignmentDTO] = []
