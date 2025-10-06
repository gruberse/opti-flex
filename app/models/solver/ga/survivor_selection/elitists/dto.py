from app.models.solver.ga.survivor_selection.base import SurvivorSelectionBase
from app.models.solver.ga.survivor_selection.dto import SurvivorSelectionDTO
from app.models.solver.ga.survivor_selection.elitists.base import ElitistsSelectionBase


class ElitistsSelectionDTO(ElitistsSelectionBase, SurvivorSelectionDTO):
    pass