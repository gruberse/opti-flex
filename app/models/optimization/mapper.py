from app.models.base_mapper import BaseMapper
from .dto import OptimizationInputDTO, OptimizationOutputDTO, OptimizationOutputBaseDTO, \
    OptimizationOutputStatisticsDTO, OptimizationOutputResultDTO
from .obj import Optimization
from ..problem.registry import ProblemMapperRegistry
from ..solver.registry import SolverMapperRegistry
from ..statistics.mapper import StatisticsMapper


class OptimizationMapper(BaseMapper):

    @staticmethod
    def to_dto(obj: Optimization) -> OptimizationOutputDTO:
        statistics = StatisticsMapper.to_dto(obj.statistics)

        problem_mapper = ProblemMapperRegistry.get_mapper(obj.problem.problem_type)
        problem = problem_mapper.to_dto(obj=obj.problem)

        solver_mapper = SolverMapperRegistry.get_mapper(obj.solver.solver_type)
        solver = solver_mapper.to_dto(obj=obj.solver)

        return OptimizationOutputDTO(
            optimization_id=obj.optimization_id,
            status=obj.status,
            statistics=statistics,
            problem=problem,
            solver=solver
        )

    @staticmethod
    def to_base_dto(obj: Optimization) -> OptimizationOutputBaseDTO:
        return OptimizationOutputBaseDTO(
            optimization_id=obj.optimization_id,
            status=obj.status,
        )

    @staticmethod
    def to_statistics_dto(obj: Optimization) -> OptimizationOutputStatisticsDTO:
        statistics_dto = StatisticsMapper.to_dto(obj.statistics)

        return OptimizationOutputStatisticsDTO(
            optimization_id=obj.optimization_id,
            status=obj.status,
            statistics=statistics_dto
        )

    @staticmethod
    def to_result_dto(obj: Optimization) -> OptimizationOutputResultDTO:
        problem_mapper = ProblemMapperRegistry.get_mapper(obj.problem.problem_type)
        problem_dto = problem_mapper.to_result_dto(obj=obj.problem)

        return OptimizationOutputResultDTO(
            optimization_id=obj.optimization_id,
            status=obj.status,
            problem=problem_dto
        )

    @staticmethod
    def from_dto(dto: OptimizationInputDTO) -> Optimization:
        problem_mapper = ProblemMapperRegistry.get_mapper(dto.problem.problem_type)
        problem = problem_mapper.from_dto(dto=dto.problem)

        solver_mapper = SolverMapperRegistry.get_mapper(dto.solver.solver_type)
        solver = solver_mapper.from_dto(dto=dto.solver)

        return Optimization(
            problem=problem,
            solver=solver,
        )
