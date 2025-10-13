from app.models.solver.ga.parent_selection.dto import ParentSelectionDTO
from app.models.solver.ga.parent_selection.tournament.base import TournamentSelectionBase


class TournamentSelectionDTO(TournamentSelectionBase, ParentSelectionDTO):
    pass
