from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.pmx.dto import PartiallyMatchedCrossoverDTO
from app.models.solver.ga.crossover.pmx.obj import PartiallyMatchedCrossover


class PartiallyMatchedCrossoverMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: PartiallyMatchedCrossover) -> PartiallyMatchedCrossoverDTO:
        return PartiallyMatchedCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )

    @staticmethod
    def from_dto(dto: PartiallyMatchedCrossoverDTO) -> PartiallyMatchedCrossover:
        return PartiallyMatchedCrossover(
            crossover_probability=dto.crossover_probability,
        )