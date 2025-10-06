from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.nsga2.dto import NSGA2ParentSelectionDTO
from app.models.solver.ga.parent_selection.nsga2.obj import NSGA2ParentSelection


class NSGA2ParentSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2ParentSelection) -> NSGA2ParentSelectionDTO:
        return NSGA2ParentSelectionDTO(
            tournament_size=obj.tournament_size,
        )

    @staticmethod
    def from_dto(dto: NSGA2ParentSelectionDTO) -> NSGA2ParentSelection:
        return NSGA2ParentSelection(
            tournament_size=dto.tournament_size,
        )