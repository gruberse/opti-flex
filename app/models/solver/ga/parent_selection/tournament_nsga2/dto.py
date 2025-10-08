from app.models.solver.ga.parent_selection.dto import ParentSelectionDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.base import NSGA2basedTournamentSelectionBase


class NSGA2BasedTournamentSelectionDTO(NSGA2basedTournamentSelectionBase, ParentSelectionDTO):
    pass
