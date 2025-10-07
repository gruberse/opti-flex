from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2SurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2SurvivalSelection


class NSGA2SurvivalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2SurvivalSelection) -> NSGA2SurvivalSelectionDTO:
        return NSGA2SurvivalSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2SurvivalSelectionDTO) -> NSGA2SurvivalSelection:
        return NSGA2SurvivalSelection()