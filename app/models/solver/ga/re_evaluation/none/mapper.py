from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.re_evaluation.none.dto import NoReEvaluationDTO
from app.models.solver.ga.re_evaluation.none.obj import NoReEvaluation


class NoReEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NoReEvaluation) -> NoReEvaluationDTO:
        return NoReEvaluationDTO()


    @staticmethod
    def from_dto(dto: NoReEvaluationDTO) -> NoReEvaluation:
        return NoReEvaluation()
