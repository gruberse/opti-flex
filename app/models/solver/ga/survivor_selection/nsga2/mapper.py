from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2basedSurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.obj import NSGA2basedSurvivorSelection


class NSGA2basedSurvivorSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2basedSurvivorSelection) -> NSGA2basedSurvivorSelectionDTO:
        return NSGA2basedSurvivorSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2basedSurvivorSelectionDTO) -> NSGA2basedSurvivorSelection:
        return NSGA2basedSurvivorSelection()