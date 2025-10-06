from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.generational.mapper import GenerationalSelectionMapper
from app.models.solver.ga.survivor_selection.nsga2_elitists.mapper import NSGA2basedElitistsSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "generational": GenerationalSelectionMapper,
        "nsga2_elitists": NSGA2basedElitistsSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)