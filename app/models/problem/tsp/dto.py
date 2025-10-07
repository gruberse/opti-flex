from typing import List

from app.models.objective.tsp.dto import TravelingSalesmanObjectiveDTO
from app.models.problem.dto import ProblemDTO
from app.models.problem.tsp.base import TravelingSalesmanProblemBase
from app.models.problem.tsp.tour.dto import TourDTO


class TravelingSalesmanProblemInputDTO(TravelingSalesmanProblemBase, ProblemDTO):
    objectives: List[TravelingSalesmanObjectiveDTO]


class TravelingSalesmanProblemOutputDTO(TravelingSalesmanProblemBase, ProblemDTO):
    objectives: List[TravelingSalesmanObjectiveDTO]
    result_tours: List[TourDTO] = []


class TravelingSalesmanProblemOutputResultDTO(TravelingSalesmanProblemBase, ProblemDTO):
    result_tours: List[TourDTO] = []
