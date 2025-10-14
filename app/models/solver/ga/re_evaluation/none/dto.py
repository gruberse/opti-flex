from app.models.solver.ga.re_evaluation.dto import ReEvaluationDTO
from app.models.solver.ga.re_evaluation.none.base import NoReEvaluationBase


class NoReEvaluationDTO(NoReEvaluationBase, ReEvaluationDTO):
    pass
