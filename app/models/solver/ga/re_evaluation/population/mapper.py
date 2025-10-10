from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.re_evaluation.population.dto import PopulationReEvaluationDTO
from app.models.solver.ga.re_evaluation.population.obj import PopulationReEvaluation


class PopulationReEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: PopulationReEvaluation) -> PopulationReEvaluationDTO:
        return PopulationReEvaluationDTO()


    @staticmethod
    def from_dto(dto: PopulationReEvaluationDTO) -> PopulationReEvaluation:
        return PopulationReEvaluation()
