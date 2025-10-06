from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.fitness_evaluation.elitists.dto import ElitistsEvaluationDTO
from app.models.solver.ga.fitness_evaluation.elitists.obj import ElitistsEvaluation


class ElitistsEvaluationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ElitistsEvaluation) -> ElitistsEvaluationDTO:
        return ElitistsEvaluationDTO(
            replace_offspring=obj.replace_offspring,
        )


    @staticmethod
    def from_dto(dto: ElitistsEvaluationDTO) -> ElitistsEvaluation:
        return ElitistsEvaluation(
            replace_offspring=dto.replace_offspring,
        )