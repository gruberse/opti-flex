from .assignment.mapper import AssignmentMapper
from .dto import AssignmentProblemInputDTO, AssignmentProblemOutputDTO, AssignmentProblemOutputResultDTO
from .obj import AssignmentProblem
from ..problem_mapper import ProblemMapper
from ...objective.ap.mapper import AssignmentObjectiveMapper


class AssignmentProblemMapper(ProblemMapper):
    @staticmethod
    def to_dto(obj: AssignmentProblem) -> AssignmentProblemOutputDTO:
        objectives = [AssignmentObjectiveMapper.to_dto(objective) for objective in obj.objectives]
        results = [AssignmentMapper.to_dto(result_list) for result_list in obj.result_assignments]

        return AssignmentProblemOutputDTO(
            objectives=objectives,
            result_assignments=results
        )

    @staticmethod
    def to_result_dto(obj: AssignmentProblem) -> AssignmentProblemOutputResultDTO:
        results = [AssignmentMapper.to_dto(result_list) for result_list in obj.result_assignments]

        return AssignmentProblemOutputResultDTO(
            result_assignments=results
        )

    @staticmethod
    def from_dto(dto: AssignmentProblemInputDTO) -> AssignmentProblem:
        objectives = [AssignmentObjectiveMapper.from_dto(objective) for objective in dto.objectives]

        return AssignmentProblem(
            objectives=objectives
        )
