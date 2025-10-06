from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2_elitists.base import NSGA2basedElitistsSelectionBase


class NSGA2BasedElitistsSelectionDTO(NSGA2basedElitistsSelectionBase, SurvivorSelectionDTO):
    pass