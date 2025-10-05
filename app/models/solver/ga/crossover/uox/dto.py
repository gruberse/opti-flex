from app.models.solver.ga.crossover.dto import CrossoverDTO
from app.models.solver.ga.crossover.uox.base import UniformOrderBasedCrossoverBase


class UniformOrderBasedCrossoverDTO(UniformOrderBasedCrossoverBase, CrossoverDTO):
    pass
