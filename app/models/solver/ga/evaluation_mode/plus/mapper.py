from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.evaluation_mode.plus.dto import PlusModeDTO
from app.models.solver.ga.evaluation_mode.plus.obj import PlusMode


class PlusModeMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: PlusMode) -> PlusModeDTO:
        return PlusModeDTO()


    @staticmethod
    def from_dto(dto: PlusModeDTO) -> PlusMode:
        return PlusMode()
