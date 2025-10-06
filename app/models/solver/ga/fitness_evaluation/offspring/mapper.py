from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.fitness_evaluation.offspring.dto import OffspringEvaluationDTO
from app.models.solver.ga.fitness_evaluation.offspring.obj import OffspringEvaluation


class OffspringEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: OffspringEvaluation) -> OffspringEvaluationDTO:
        return OffspringEvaluationDTO()

    @staticmethod
    def from_dto(dto: OffspringEvaluationDTO) -> OffspringEvaluation:
        return OffspringEvaluation()