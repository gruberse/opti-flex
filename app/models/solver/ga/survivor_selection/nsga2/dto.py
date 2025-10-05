from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2SelectionBase


class NSGA2SelectionDTO(NSGA2SelectionBase, SurvivorSelectionDTO):
    pass