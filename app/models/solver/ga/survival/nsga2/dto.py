from app.models.solver.ga.survival.dto import SurvivalDTO
from app.models.solver.ga.survival.nsga2.base import NSGA2basedSurvivalBase


class NSGA2basedSurvivalDTO(NSGA2basedSurvivalBase, SurvivalDTO):
    pass