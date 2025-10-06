from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2SurvivorSelection


class NSGA2SurvivorSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2SurvivorSelection) -> NSGA2SurvivorSelectionDTO:
        return NSGA2SurvivorSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2SurvivorSelectionDTO) -> NSGA2SurvivorSelection:
        return NSGA2SurvivorSelection()