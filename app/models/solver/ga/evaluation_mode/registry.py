from app.models.base_mapper import BaseMapper
from app.models.solver.ga.evaluation_mode.plus.mapper import PlusModeMapper
from app.models.solver.ga.evaluation_mode.comma.mapper import CommaModeMapper


class EvaluationModeMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "comma": CommaModeMapper,
        "plus": PlusModeMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return EvaluationModeMapperRegistry._mapper_registry.get(survivor_selection_type)