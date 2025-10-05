from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.age_based.mapper import AgeBasedSelectionMapper
from app.models.solver.ga.survivor_selection.nsga2.mapper import NSGA2basedSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "age_based": AgeBasedSelectionMapper,
        "nsga2": NSGA2basedSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)