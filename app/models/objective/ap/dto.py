from typing import List

from .base import AssignmentObjectiveBase
from ..dto import ObjectiveDTO


class AssignmentObjectiveDTO(AssignmentObjectiveBase, ObjectiveDTO):
    weights: List[List[int]]
