from app.models.solver.ga.environmental_selection.dto import EnvironmentalSelectionDTO
from app.models.solver.ga.environmental_selection.nsga2.base import NSGA2basedEnvironmentalSelectionBase


class NSGA2BasedEnvironmentalSelectionDTO(NSGA2basedEnvironmentalSelectionBase, EnvironmentalSelectionDTO):
    pass