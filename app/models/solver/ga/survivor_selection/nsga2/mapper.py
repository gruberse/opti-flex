from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2BasedSurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2BasedSurvivalSelection


class NSGA2SurvivalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2BasedSurvivalSelection) -> NSGA2BasedSurvivalSelectionDTO:
        return NSGA2BasedSurvivalSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2BasedSurvivalSelectionDTO) -> NSGA2BasedSurvivalSelection:
        return NSGA2BasedSurvivalSelection()