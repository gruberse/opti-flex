from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.crossover.uox.obj import UniformOrderBasedCrossover


class UniformOrderBasedCrossoverMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: UniformOrderBasedCrossover) -> UniformOrderBasedCrossoverDTO:
        return UniformOrderBasedCrossoverDTO(
            crossover_probability=obj.crossover_probability,
            keep_genes_probability=obj.keep_genes_probability,
        )

    @staticmethod
    def from_dto(dto: UniformOrderBasedCrossoverDTO) -> UniformOrderBasedCrossover:
        return UniformOrderBasedCrossover(
            crossover_probability=dto.crossover_probability,
            keep_genes_probability=dto.keep_genes_probability,
        )