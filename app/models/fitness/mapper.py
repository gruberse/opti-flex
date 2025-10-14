from typing import Any

from app.models.base_mapper import BaseMapper
from .dto import FitnessDTO
from .obj import Fitness


class FitnessMapper(BaseMapper):

    @staticmethod
    def to_dto(obj: Fitness) -> FitnessDTO:
        return FitnessDTO(
            objective_id=obj.objective_id,
            actual_fitness=obj.actual_fitness,
            estimated_fitness=obj.estimated_fitness,
        )

    @staticmethod
    def from_dto(**kwargs) -> Any:
        pass
