from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.age.mapper import AgeBasedSelectionMapper
from app.models.solver.ga.survivor_selection.nsga2.mapper import NSGA2SurvivorSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "age": AgeBasedSelectionMapper,
        "nsga2": NSGA2SurvivorSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)