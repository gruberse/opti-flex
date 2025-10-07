from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2SurvivalSelectionBase


class NSGA2SurvivalSelectionDTO(NSGA2SurvivalSelectionBase, SurvivorSelectionDTO):
    pass