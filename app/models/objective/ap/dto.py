from typing import List

from .base import AssignmentProblemObjectiveBase
from ..dto import ObjectiveDTO


class AssignmentProblemObjectiveDTO(AssignmentProblemObjectiveBase, ObjectiveDTO):
    weights: List[List[int]]
