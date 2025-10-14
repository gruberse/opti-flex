from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survival.truncation.dto import TruncationSurvivalDTO
from app.models.solver.ga.survival.truncation.obj import TruncationSurvival


class TruncationSurvivalMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TruncationSurvival) -> TruncationSurvivalDTO:
        return TruncationSurvivalDTO()

    @staticmethod
    def from_dto(dto: TruncationSurvivalDTO) -> TruncationSurvival:
        return TruncationSurvival()