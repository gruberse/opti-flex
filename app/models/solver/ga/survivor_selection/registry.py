from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survivor_selection.best.mapper import BestIndividualsSelectionMapper
from app.models.solver.ga.survivor_selection.nsga2.mapper import NSGA2SurvivalSelectionMapper


class SurvivorSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "best": BestIndividualsSelectionMapper,
        "nsga2": NSGA2SurvivalSelectionMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return SurvivorSelectionMapperRegistry._mapper_registry.get(survivor_selection_type)