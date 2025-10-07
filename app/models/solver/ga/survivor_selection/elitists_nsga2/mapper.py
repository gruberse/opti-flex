from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.elitists_nsga2.dto import NSGA2BasedElitistsSelectionDTO
from app.models.solver.ga.survivor_selection.elitists_nsga2.obj import NSGA2BasedElitistsSelection


class NSGA2basedElitistsSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2BasedElitistsSelection) -> NSGA2BasedElitistsSelectionDTO:
        return NSGA2BasedElitistsSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2BasedElitistsSelectionDTO) -> NSGA2BasedElitistsSelection:
        return NSGA2BasedElitistsSelection()