from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.mutation.swap.obj import SwapMutation


class SwapMutationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: SwapMutation) -> SwapMutationDTO:
        return SwapMutationDTO(
            mutation_probability=obj.mutation_probability,
        )


    @staticmethod
    def from_dto(dto: SwapMutationDTO) -> SwapMutation:
        return SwapMutation(
            mutation_probability=dto.mutation_probability,
        )