from app.models.solver.ga.re_evaluation.dto import ReEvaluationDTO
from app.models.solver.ga.re_evaluation.elitists.base import ElitistsReEvaluationBase


class ElitistsReEvaluationDTO(ElitistsReEvaluationBase, ReEvaluationDTO):
    pass
