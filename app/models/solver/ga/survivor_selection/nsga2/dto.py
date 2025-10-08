from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.base import NSGA2basedSurvivalSelectionBase


class NSGA2BasedSurvivalSelectionDTO(NSGA2basedSurvivalSelectionBase, SurvivorSelectionDTO):
    pass