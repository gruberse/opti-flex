
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.truncation.base import TruncationSelectionBase


class TruncationSelectionDTO(TruncationSelectionBase, SurvivorSelectionDTO):
    pass