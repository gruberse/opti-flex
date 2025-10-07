from app.models.objective.tsp.mapper import TravelingSalesmanObjectiveMapper
from app.models.problem.problem_mapper import ProblemMapper
from app.models.problem.tsp.dto import TravelingSalesmanProblemOutputResultDTO, TravelingSalesmanProblemOutputDTO, \
    TravelingSalesmanProblemInputDTO
from app.models.problem.tsp.obj import TravelingSalesmanProblem
from app.models.problem.tsp.tour.mapper import TourMapper


class TravelingSalesmanProblemMapper(ProblemMapper):
    @staticmethod
    def to_result_dto(obj: TravelingSalesmanProblem) -> TravelingSalesmanProblemOutputResultDTO:
        tours = [TourMapper.to_dto(tour) for tour in obj.result_tours]
        return TravelingSalesmanProblemOutputResultDTO(
            result_tours=tours
        )

    @staticmethod
    def to_dto(obj: TravelingSalesmanProblem) -> TravelingSalesmanProblemOutputDTO:
        objectives = [TravelingSalesmanObjectiveMapper.to_dto(objective) for objective in obj.objectives]
        tours = [TourMapper.to_dto(tour) for tour in obj.result_tours]
        return TravelingSalesmanProblemOutputDTO(
            objectives=objectives,
            result_tours=tours
        )

    @staticmethod
    def from_dto(dto: TravelingSalesmanProblemInputDTO) -> TravelingSalesmanProblem:
        objectives = [TravelingSalesmanObjectiveMapper.from_dto(objective) for objective in dto.objectives]
        return TravelingSalesmanProblem(
            objectives=objectives,
        )
