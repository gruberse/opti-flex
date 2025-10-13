from app.models.base_mapper import BaseMapper
from app.models.solver.ga.reduction.nsga2.mapper import NSGA2basedReductionMapper
from app.models.solver.ga.reduction.truncation.mapper import TruncationReductionMapper


class ReductionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "truncation": TruncationReductionMapper,
        "nsga2": NSGA2basedReductionMapper,
    }


    @staticmethod
    def get_mapper(reduction_type: str) -> BaseMapper:
        return ReductionMapperRegistry._mapper_registry.get(reduction_type)