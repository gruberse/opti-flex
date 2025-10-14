from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.cx.mapper import CycleCrossoverMapper
from app.models.solver.ga.crossover.erx.mapper import EdgeRecombinationCrossoverMapper
from app.models.solver.ga.crossover.ox.mapper import OrderCrossoverMapper
from app.models.solver.ga.crossover.pmx.mapper import PartiallyMappedCrossoverMapper
from app.models.solver.ga.crossover.uox.mapper import UniformOrderBasedCrossoverMapper


class CrossoverMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "cx": CycleCrossoverMapper,
        "ox": OrderCrossoverMapper,
        "pmx": PartiallyMappedCrossoverMapper,
        "uox": UniformOrderBasedCrossoverMapper,
        "erx": EdgeRecombinationCrossoverMapper,
    }


    @staticmethod
    def get_mapper(crossover_type: str) -> BaseMapper:
        return CrossoverMapperRegistry._mapper_registry.get(crossover_type)