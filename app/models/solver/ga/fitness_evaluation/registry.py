from app.models.base_mapper import BaseMapper
from app.models.solver.ga.fitness_evaluation.combined.mapper import CombinedEvaluationMapper
from app.models.solver.ga.fitness_evaluation.elitists.mapper import ElitistsEvaluationMapper
from app.models.solver.ga.fitness_evaluation.offspring.mapper import OffspringEvaluationMapper


class FitnessEvaluationMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "offspring": OffspringEvaluationMapper,
        "elitists": ElitistsEvaluationMapper,
        "combined": CombinedEvaluationMapper,
    }


    @staticmethod
    def get_mapper(fitness_evaluation_type: str) -> BaseMapper:
        return FitnessEvaluationMapperRegistry._mapper_registry.get(fitness_evaluation_type)