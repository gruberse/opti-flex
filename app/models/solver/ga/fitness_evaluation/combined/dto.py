from app.models.solver.ga.fitness_evaluation.base import FitnessEvaluationBase
from app.models.solver.ga.fitness_evaluation.combined.base import CombinedEvaluationBase
from app.models.solver.ga.fitness_evaluation.dto import FitnessEvaluationDTO


class CombinedEvaluationDTO(CombinedEvaluationBase, FitnessEvaluationDTO):
    pass
