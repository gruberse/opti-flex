from app.models.base_mapper import BaseMapper

from app.models.solver.ga.survivor_selection.elitists.mapper import ElitistsSelectionMapper
from app.models.solver.ga.survivor_selection.nsga2_elitists.mapper import NSGA2basedElitistsSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "elitists": ElitistsSelectionMapper,
        "nsga2_elitists": NSGA2basedElitistsSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)