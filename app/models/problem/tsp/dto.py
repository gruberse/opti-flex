from typing import List

from app.models.objective.tsp.dto import TravelingSalesmanProblemObjectiveDTO
from app.models.problem.dto import ProblemDTO
from app.models.problem.tsp.base import TravelingSalesmanProblemBase
from app.models.problem.tsp.tour.dto import TourDTO


class TravelingSalesmanProblemInputDTO(TravelingSalesmanProblemBase, ProblemDTO):
    objectives: List[TravelingSalesmanProblemObjectiveDTO]


class TravelingSalesmanProblemOutputDTO(TravelingSalesmanProblemBase, ProblemDTO):
    objectives: List[TravelingSalesmanProblemObjectiveDTO]
    result_tours: List[TourDTO] = []


class TravelingSalesmanProblemOutputResultDTO(TravelingSalesmanProblemBase, ProblemDTO):
    result_tours: List[TourDTO] = []
