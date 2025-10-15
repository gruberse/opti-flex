from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.fitness.mapper import FitnessMapper
from app.models.problem.tsp.tour.dto import TourDTO
from app.models.problem.tsp.tour.obj import Tour


class TourMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: Tour) -> TourDTO:
        fitness_list = [FitnessMapper.to_dto(fitness) for fitness in obj.fitness_list]

        return TourDTO(
            cities=obj.cities,
            fitness_list=fitness_list,
        )

    @staticmethod
    def from_dto(**kwargs) -> Any:
        pass
