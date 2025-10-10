from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.erx.dto import EdgeRecombinationCrossoverDTO
from app.models.solver.ga.crossover.erx.obj import EdgeRecombinationCrossover


class EdgeRecombinationCrossoverMapper(BaseMapper):

    @staticmethod
    def to_dto(obj: EdgeRecombinationCrossover) -> EdgeRecombinationCrossoverDTO:
        return EdgeRecombinationCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )

    @staticmethod
    def from_dto(dto: EdgeRecombinationCrossoverDTO) -> EdgeRecombinationCrossover:
        return EdgeRecombinationCrossover(
            crossover_probability=dto.crossover_probability,
        )