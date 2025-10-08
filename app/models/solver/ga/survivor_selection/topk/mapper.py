from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.topk.dto import TopKSelectionDTO
from app.models.solver.ga.survivor_selection.topk.obj import TopKSelection


class TopKSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TopKSelection) -> TopKSelectionDTO:
        return TopKSelectionDTO()

    @staticmethod
    def from_dto(dto: TopKSelectionDTO) -> TopKSelection:
        return TopKSelection()