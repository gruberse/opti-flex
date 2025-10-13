from app.models.solver.ga.reduction.dto import ReductionDTO
from app.models.solver.ga.reduction.nsga2.base import NSGA2basedReductionBase


class NSGA2BasedReductionDTO(NSGA2basedReductionBase, ReductionDTO):
    pass