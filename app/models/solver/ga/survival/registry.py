from app.models.base_mapper import BaseMapper
from app.models.solver.ga.survival.nsga2.mapper import NSGA2basedSurvivalMapper
from app.models.solver.ga.survival.truncation.mapper import TruncationSurvivalMapper


class SurvivalMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "truncation": TruncationSurvivalMapper,
        "nsga2": NSGA2basedSurvivalMapper,
    }


    @staticmethod
    def get_mapper(survival_type: str) -> BaseMapper:
        return SurvivalMapperRegistry._mapper_registry.get(survival_type)