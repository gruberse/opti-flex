from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.re_evaluation.elitists.dto import ElitistsReEvaluationDTO
from app.models.solver.ga.re_evaluation.elitists.obj import ElitistsReEvaluation


class ElitistsReEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ElitistsReEvaluation) -> ElitistsReEvaluationDTO:
        return ElitistsReEvaluationDTO(
            n_elitists=obj.n_elitists,
        )

    @staticmethod
    def from_dto(dto: ElitistsReEvaluationDTO) -> ElitistsReEvaluation:
        return ElitistsReEvaluation(
            n_elitists=dto.n_elitists,
        )
