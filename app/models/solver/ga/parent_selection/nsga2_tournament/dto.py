from app.models.solver.ga.parent_selection.dto import ParentSelectionDTO
from app.models.solver.ga.parent_selection.nsga2_tournament.base import NSGA2basedTournamentSelectionBase


class NSGA2BasedTournamentSelectionDTO(NSGA2basedTournamentSelectionBase, ParentSelectionDTO):
    pass
