from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.fitness_evaluation.combined.dto import CombinedEvaluationDTO
from app.models.solver.ga.fitness_evaluation.combined.obj import CombinedEvaluation


class CombinedEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: CombinedEvaluation) -> CombinedEvaluationDTO:
        return CombinedEvaluationDTO()


    @staticmethod
    def from_dto(dto: CombinedEvaluationDTO) -> CombinedEvaluation:
        return CombinedEvaluation()