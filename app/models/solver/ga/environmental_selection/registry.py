from app.models.base_mapper import BaseMapper
from app.models.solver.ga.environmental_selection.nsga2.mapper import NSGA2basedEnvironmentalSelectionMapper
from app.models.solver.ga.environmental_selection.truncation.mapper import TruncationSelectionMapper


class EnvironmentalSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "truncation": TruncationSelectionMapper,
        "nsga2": NSGA2basedEnvironmentalSelectionMapper,
    }


    @staticmethod
    def get_mapper(environmental_selection_type: str) -> BaseMapper:
        return EnvironmentalSelectionMapperRegistry._mapper_registry.get(environmental_selection_type)