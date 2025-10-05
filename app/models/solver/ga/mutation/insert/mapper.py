from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.insert.obj import InsertMutation


class InsertMutationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: InsertMutation) -> InsertMutationDTO:
        return InsertMutationDTO(
            mutation_probability=obj.mutation_probability,
        )


    @staticmethod
    def from_dto(dto: InsertMutationDTO) -> InsertMutation:
        return InsertMutation(
            mutation_probability=dto.mutation_probability,
        )