from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.evaluation_mode.comma.dto import CommaModeDTO
from app.models.solver.ga.evaluation_mode.comma.obj import CommaMode


class CommaModeMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: CommaMode) -> CommaModeDTO:
        return CommaModeDTO()

    @staticmethod
    def from_dto(dto: CommaModeDTO) -> CommaMode:
        return CommaMode()
