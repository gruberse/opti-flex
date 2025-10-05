from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2SelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2Selection


class NSGA2basedSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2Selection) -> NSGA2SelectionDTO:
        return NSGA2SelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2SelectionDTO) -> NSGA2Selection:
        return NSGA2Selection()