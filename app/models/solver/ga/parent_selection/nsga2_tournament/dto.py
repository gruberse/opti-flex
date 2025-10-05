from app.models.solver.ga.parent_selection.dto import ParentSelectionDTO
from app.models.solver.ga.parent_selection.nsga2_tournament.base import NSGA2TournamentSelectionBase


class NSGA2TournamentSelectionDTO(NSGA2TournamentSelectionBase, ParentSelectionDTO):
    pass
