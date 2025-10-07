from app.models.solver.ga.parent_selection.dto import ParentSelectionDTO
from app.models.solver.ga.parent_selection.nsga2.base import NSGA2ParentSelectionBase


class NSGA2ParentSelectionDTO(NSGA2ParentSelectionBase, ParentSelectionDTO):
    pass
