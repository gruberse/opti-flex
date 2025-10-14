from typing import Any

from app.config import config
from app.models.base_mapper import BaseMapper
from .dto import PopulationDTO
from .obj import Population
from ..individual.mapper import IndividualMapper


class PopulationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: Population) -> PopulationDTO:
        individuals = []
        statistics_individuals = config.getboolean("statistics", "individuals")
        if statistics_individuals == True:
            individuals = [IndividualMapper.to_dto(individual) for individual in obj.individuals]

        non_dominated_individuals = [IndividualMapper.to_dto(individual) for individual in obj.non_dominated_individuals]

        return PopulationDTO(
            population_id=obj.population_id,
            start_time=obj.start_time,
            end_time=obj.end_time,
            non_dominated_individuals=non_dominated_individuals,
            individuals=individuals,
        )

    @staticmethod
    def from_dto(**kwargs) -> Any:
        pass
