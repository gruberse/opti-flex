from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2basedSurvivorSelectionBase


class NSGA2basedSurvivorSelectionDTO(NSGA2basedSurvivorSelectionBase, SurvivorSelectionDTO):
    pass