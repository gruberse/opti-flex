from app.models.solver.ga.survivor_selection.age.base import AgeBasedSelectionBase
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO


class AgeBasedSelectionDTO(AgeBasedSelectionBase, SurvivorSelectionDTO):
    pass
