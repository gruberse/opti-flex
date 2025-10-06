from app.models.solver.ga.fitness_evaluation.dto import FitnessEvaluationDTO
from app.models.solver.ga.fitness_evaluation.elitists.base import ElitistsEvaluationBase


class ElitistsEvaluationDTO(ElitistsEvaluationBase, FitnessEvaluationDTO):
    pass