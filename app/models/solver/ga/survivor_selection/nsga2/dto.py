from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2SurvivorSelectionBase


class NSGA2SurvivorSelectionDTO(NSGA2SurvivorSelectionBase, SurvivorSelectionDTO):
    pass