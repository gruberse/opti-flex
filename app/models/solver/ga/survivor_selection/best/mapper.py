from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.best.dto import BestIndividualsSelectionDTO
from app.models.solver.ga.survivor_selection.best.obj import BestIndividualsSelection


class BestIndividualsSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: BestIndividualsSelection) -> BestIndividualsSelectionDTO:
        return BestIndividualsSelectionDTO()

    @staticmethod
    def from_dto(dto: BestIndividualsSelectionDTO) -> BestIndividualsSelection:
        return BestIndividualsSelection()