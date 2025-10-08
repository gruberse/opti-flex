
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.topk.base import TopKSurvivalSelectionBase


class TopKSurvivalSelectionDTO(TopKSurvivalSelectionBase, SurvivorSelectionDTO):
    pass