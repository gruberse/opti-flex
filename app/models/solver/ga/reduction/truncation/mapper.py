from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.reduction.truncation.dto import TruncationReductionDTO
from app.models.solver.ga.reduction.truncation.obj import TruncationReduction


class TruncationReductionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TruncationReduction) -> TruncationReductionDTO:
        return TruncationReductionDTO()

    @staticmethod
    def from_dto(dto: TruncationReductionDTO) -> TruncationReduction:
        return TruncationReduction()