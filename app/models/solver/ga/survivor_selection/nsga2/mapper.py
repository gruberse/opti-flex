from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2basedSurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2basedSurvivalSelection


class NSGA2basedSurvivalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2basedSurvivalSelection) -> NSGA2basedSurvivalSelectionDTO:
        return NSGA2basedSurvivalSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2basedSurvivalSelectionDTO) -> NSGA2basedSurvivalSelection:
        return NSGA2basedSurvivalSelection()