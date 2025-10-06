from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.elitists.dto import ElitistsSelectionDTO
from app.models.solver.ga.survivor_selection.elitists.obj import ElitistsSelection


class ElitistsSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ElitistsSelection) -> ElitistsSelectionDTO:
        return ElitistsSelectionDTO()

    @staticmethod
    def from_dto(dto: ElitistsSelectionDTO) -> ElitistsSelection:
        return ElitistsSelection()