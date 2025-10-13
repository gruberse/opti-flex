
from app.models.solver.ga.reduction.dto import ReductionDTO
from app.models.solver.ga.reduction.truncation.base import TruncationReductionBase


class TruncationReductionDTO(TruncationReductionBase, ReductionDTO):
    pass