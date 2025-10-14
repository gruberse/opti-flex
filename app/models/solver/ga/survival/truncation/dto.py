
from app.models.solver.ga.survival.dto import SurvivalDTO
from app.models.solver.ga.survival.truncation.base import TruncationSurvivalBase


class TruncationSurvivalDTO(TruncationSurvivalBase, SurvivalDTO):
    pass