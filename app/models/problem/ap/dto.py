from typing import List

from .base import AssignmentProblemBase
from .assignment.dto import AssignmentDTO
from ..dto import ProblemDTO
from ...objective.ap.dto import AssignmentObjectiveDTO


class AssignmentProblemInputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentObjectiveDTO]


class AssignmentProblemOutputDTO(AssignmentProblemBase, ProblemDTO):
    objectives: List[AssignmentObjectiveDTO]
    result_assignments: List[AssignmentDTO] = []


class AssignmentProblemOutputResultDTO(AssignmentProblemBase, ProblemDTO):
    result_assignments: List[AssignmentDTO] = []
