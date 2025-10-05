from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.ox.obj import OrderCrossover


class OrderCrossoverMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: OrderCrossover) -> OrderCrossoverDTO:
        return OrderCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )

    @staticmethod
    def from_dto(dto: OrderCrossoverDTO) -> OrderCrossover:
        return OrderCrossover(
            crossover_probability=dto.crossover_probability,
        )