from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survival.nsga2.dto import NSGA2basedSurvivalDTO
from app.models.solver.ga.survival.nsga2.obj import NSGA2basedSurvival


class NSGA2basedSurvivalMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2basedSurvival) -> NSGA2basedSurvivalDTO:
        return NSGA2basedSurvivalDTO()


    @staticmethod
    def from_dto(dto: NSGA2basedSurvivalDTO) -> NSGA2basedSurvival:
        return NSGA2basedSurvival()