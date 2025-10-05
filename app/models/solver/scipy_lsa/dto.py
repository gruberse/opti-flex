from typing import List, Optional

from .base import ScipyLinearSumAssignmentBase
from .weights.dto import WeightsDTO
from ..dto import SolverDTO


class ScipyLinearSumAssignmentDTO(ScipyLinearSumAssignmentBase, SolverDTO):
    weights_list: Optional[List[WeightsDTO]] = None
