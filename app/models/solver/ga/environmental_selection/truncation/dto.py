
from app.models.solver.ga.environmental_selection.dto import EnvironmentalSelectionDTO
from app.models.solver.ga.environmental_selection.truncation.base import TruncationSelectionBase


class TruncationSelectionDTO(TruncationSelectionBase, EnvironmentalSelectionDTO):
    pass