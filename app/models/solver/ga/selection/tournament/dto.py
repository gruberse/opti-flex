from app.models.solver.ga.selection.dto import SelectionDTO
from app.models.solver.ga.selection.tournament.base import TournamentSelectionBase


class TournamentSelectionDTO(TournamentSelectionBase, SelectionDTO):
    pass
