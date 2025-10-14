from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.pmx.dto import PartiallyMappedCrossoverDTO
from app.models.solver.ga.crossover.pmx.obj import PartiallyMappedCrossover


class PartiallyMappedCrossoverMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: PartiallyMappedCrossover) -> PartiallyMappedCrossoverDTO:
        return PartiallyMappedCrossoverDTO(
            crossover_probability=obj.crossover_probability,
        )

    @staticmethod
    def from_dto(dto: PartiallyMappedCrossoverDTO) -> PartiallyMappedCrossover:
        return PartiallyMappedCrossover(
            crossover_probability=dto.crossover_probability,
        )