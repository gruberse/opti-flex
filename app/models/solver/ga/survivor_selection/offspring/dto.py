from app.models.solver.ga.survivor_selection.offspring.base import OffspringSelectionBase
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO


class OffspringSelectionDTO(OffspringSelectionBase, SurvivorSelectionDTO):
    pass
