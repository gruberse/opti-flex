from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.truncation.dto import TruncationSelectionDTO
from app.models.solver.ga.survivor_selection.truncation.obj import TruncationSelection


class TruncationSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TruncationSelection) -> TruncationSelectionDTO:
        return TruncationSelectionDTO()

    @staticmethod
    def from_dto(dto: TruncationSelectionDTO) -> TruncationSelection:
        return TruncationSelection()