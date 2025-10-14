from app.models.base_mapper import BaseMapper
from app.models.solver.ga.environmental_selection.nsga2.dto import NSGA2BasedEnvironmentalSelectionDTO
from app.models.solver.ga.environmental_selection.nsga2.obj import NSGA2BasedEnvironmentalSelection


class NSGA2basedEnvironmentalSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2BasedEnvironmentalSelection) -> NSGA2BasedEnvironmentalSelectionDTO:
        return NSGA2BasedEnvironmentalSelectionDTO()


    @staticmethod
    def from_dto(dto: NSGA2BasedEnvironmentalSelectionDTO) -> NSGA2BasedEnvironmentalSelection:
        return NSGA2BasedEnvironmentalSelection()