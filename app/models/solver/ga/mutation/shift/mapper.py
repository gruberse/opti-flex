from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.shift.obj import ShiftMutation


class ShiftMutationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ShiftMutation) -> ShiftMutationDTO:
        return ShiftMutationDTO(
            mutation_probability=obj.mutation_probability,
        )

    @staticmethod
    def from_dto(dto: ShiftMutationDTO) -> ShiftMutation:
        return ShiftMutation(
            mutation_probability=dto.mutation_probability,
        )