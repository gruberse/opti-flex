from app.models.solver.ga.survivor_selection.generational.base import GenerationalSelectionBase
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO


class GenerationalSelectionDTO(GenerationalSelectionBase, SurvivorSelectionDTO):
    pass
