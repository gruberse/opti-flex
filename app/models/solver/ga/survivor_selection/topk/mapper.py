from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.topk.dto import TopKSurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.topk.obj import TopKSurvivalSelection


class TopKSurvivalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TopKSurvivalSelection) -> TopKSurvivalSelectionDTO:
        return TopKSurvivalSelectionDTO()

    @staticmethod
    def from_dto(dto: TopKSurvivalSelectionDTO) -> TopKSurvivalSelection:
        return TopKSurvivalSelection()