from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.offspring.dto import OffspringSelectionDTO
from app.models.solver.ga.survivor_selection.offspring.obj import OffspringSelection


class OffspringSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: OffspringSelection) -> OffspringSelectionDTO:
        return OffspringSelectionDTO(
        )


    @staticmethod
    def from_dto(dto: OffspringSelectionDTO) -> OffspringSelection:
        return OffspringSelection(

        )