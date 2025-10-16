from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.ex.dto import EdgeCrossoverDTO
from app.models.solver.ga.crossover.ex.obj import EdgeCrossover


class EdgeCrossoverMapper(BaseMapper):

    @staticmethod
    def to_dto(obj: EdgeCrossover) -> EdgeCrossoverDTO:
        return EdgeCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )

    @staticmethod
    def from_dto(dto: EdgeCrossoverDTO) -> EdgeCrossover:
        return EdgeCrossover(
            crossover_probability=dto.crossover_probability,
        )