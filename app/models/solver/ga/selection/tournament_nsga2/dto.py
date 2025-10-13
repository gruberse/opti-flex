from app.models.solver.ga.selection.dto import SelectionDTO
from app.models.solver.ga.selection.tournament_nsga2.base import NSGA2basedTournamentSelectionBase


class NSGA2basedTournamentSelectionDTO(NSGA2basedTournamentSelectionBase, SelectionDTO):
    pass
