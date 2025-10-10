from app.models.base_mapper import BaseMapper
from app.models.solver.ga.re_evaluation.elitists.mapper import ElitistsReEvaluationMapper
from app.models.solver.ga.re_evaluation.population.mapper import PopulationReEvaluationMapper


class ReEvaluationMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "population": PopulationReEvaluationMapper,
        "elitists": ElitistsReEvaluationMapper,
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return ReEvaluationMapperRegistry._mapper_registry.get(survivor_selection_type)