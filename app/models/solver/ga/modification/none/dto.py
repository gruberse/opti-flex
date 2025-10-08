from app.models.solver.ga.modification.dto import ModificationDTO
from app.models.solver.ga.modification.none.base import NoneModificationBase


class NoneModificationDTO(NoneModificationBase, ModificationDTO):
    pass
