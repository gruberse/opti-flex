from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.inversion.obj import InversionMutation


class InversionMutationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: InversionMutation) -> InversionMutationDTO:
        return InversionMutationDTO(
            mutation_probability=obj.mutation_probability,
        )

    @staticmethod
    def from_dto(dto: InversionMutationDTO) -> InversionMutation:
        return InversionMutation(
            mutation_probability=dto.mutation_probability,
        )