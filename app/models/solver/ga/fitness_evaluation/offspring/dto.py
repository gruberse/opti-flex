from app.models.solver.ga.fitness_evaluation.dto import FitnessEvaluationDTO
from app.models.solver.ga.fitness_evaluation.offspring.base import OffspringEvaluationBase


class OffspringEvaluationDTO(OffspringEvaluationBase, FitnessEvaluationDTO):
    pass