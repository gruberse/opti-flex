from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.scramble.obj import ScrambleMutation


class ScrambleMutationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ScrambleMutation) -> ScrambleMutationDTO:
        return ScrambleMutationDTO(
            mutation_probability=obj.mutation_probability,
        )


    @staticmethod
    def from_dto(dto: ScrambleMutationDTO) -> ScrambleMutation:
        return ScrambleMutation(
            mutation_probability=dto.mutation_probability,
        )