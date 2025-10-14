from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.fitness.mapper import FitnessMapper
from .dto import IndividualDTO
from .obj import Individual


class IndividualMapper(BaseMapper):

    @staticmethod
    def to_dto(obj: Individual) -> IndividualDTO:
        fitness_list = [FitnessMapper.to_dto(fitness) for fitness in obj.fitness_list]

        return IndividualDTO(
            fitness_list=fitness_list,
        )

    @staticmethod
    def from_dto(**kwargs) -> Any:
        pass
