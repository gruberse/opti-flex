from typing import List

from .assignment.dto import AssignmentDTO
from .base import AssignmentProblemBase
from ..dto import ProblemDTO
from ...objective.ap.dto import AssignmentObjectiveDTO


class AssignmentProblemInputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentObjectiveDTO]


class AssignmentProblemOutputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentObjectiveDTO]
    result_assignments: List[AssignmentDTO] = []


class AssignmentProblemOutputResultDTO(AssignmentProblemBase, ProblemDTO):
    result_assignments: List[AssignmentDTO] = []
