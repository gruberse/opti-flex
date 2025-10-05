from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.age_based.dto import AgeBasedSelectionDTO
from app.models.solver.ga.survivor_selection.age_based.obj import AgeBasedSelection


class AgeBasedSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: AgeBasedSelection) -> AgeBasedSelectionDTO:
        return AgeBasedSelectionDTO(
        )


    @staticmethod
    def from_dto(dto: AgeBasedSelectionDTO) -> AgeBasedSelection:
        return AgeBasedSelection(

        )