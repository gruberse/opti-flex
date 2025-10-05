from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.cx.obj import CycleCrossover


class CycleCrossoverMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: CycleCrossover) -> CycleCrossoverDTO:
        return CycleCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )


    @staticmethod
    def from_dto(dto: CycleCrossoverDTO) -> CycleCrossover:
        return CycleCrossover(
            crossover_probability=dto.crossover_probability,
        )