from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.generational.dto import GenerationalSelectionDTO
from app.models.solver.ga.survivor_selection.generational.obj import GenerationalSelection


class GenerationalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: GenerationalSelection) -> GenerationalSelectionDTO:
        return GenerationalSelectionDTO(
        )


    @staticmethod
    def from_dto(dto: GenerationalSelectionDTO) -> GenerationalSelection:
        return GenerationalSelection(

        )