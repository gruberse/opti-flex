from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.nsga2.mapper import NSGA2SurvivalSelectionMapper
from app.models.solver.ga.survivor_selection.topk.mapper import TopKSurvivalSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "topk": TopKSurvivalSelectionMapper,
        "nsga2": NSGA2SurvivalSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)