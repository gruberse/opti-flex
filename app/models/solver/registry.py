from app.models.base_mapper import BaseMapper


from .ga.mapper import GeneticAlgorithmMapper
from .scipy_lsa.mapper import ScipyLinearSumAssignmentMapper


class SolverMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "scipy_lsa": ScipyLinearSumAssignmentMapper,
        "ga": GeneticAlgorithmMapper,
    }

    @staticmethod
    def get_mapper(framework_type: str) -> BaseMapper:
        return SolverMapperRegistry._mapper_registry.get(framework_type)
