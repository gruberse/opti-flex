from typing import Union

from pydantic import Field

from .base import OptimizationBase
from ..problem.ap.dto import AssignmentProblemInputDTO, AssignmentProblemOutputDTO, AssignmentProblemOutputResultDTO
from ..problem.tsp.dto import TravelingSalesmanProblemInputDTO, TravelingSalesmanProblemOutputDTO, \
    TravelingSalesmanProblemOutputResultDTO
from ..solver.ga.dto import GeneticAlgorithmDTO
from ..solver.scipy_lsa.dto import ScipyLinearSumAssignmentDTO
from ..statistics.dto import StatisticsDTO


class OptimizationInputDTO(OptimizationBase):
    problem: Union[TravelingSalesmanProblemInputDTO, AssignmentProblemInputDTO] = Field(discriminator='problem_type')
    solver: Union[ScipyLinearSumAssignmentDTO, GeneticAlgorithmDTO] = Field(discriminator='solver_type')


class OptimizationOutputDTO(OptimizationBase):
    problem: Union[TravelingSalesmanProblemOutputDTO, AssignmentProblemOutputDTO]
    solver: Union[ScipyLinearSumAssignmentDTO, GeneticAlgorithmDTO]
    statistics: StatisticsDTO


class OptimizationOutputBaseDTO(OptimizationBase):
    pass


class OptimizationOutputStatisticsDTO(OptimizationBase):
    statistics: StatisticsDTO


class OptimizationOutputResultDTO(OptimizationBase):
    problem: Union[TravelingSalesmanProblemOutputResultDTO, AssignmentProblemOutputResultDTO]
