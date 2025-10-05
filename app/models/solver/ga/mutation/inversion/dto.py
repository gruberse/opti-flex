from app.models.solver.ga.mutation.dto import MutationDTO
from app.models.solver.ga.mutation.inversion.base import InversionMutationBase


class InversionMutationDTO(InversionMutationBase, MutationDTO):
    pass
