from typing import List

from app.models.objective.dto import ObjectiveDTO
from app.models.objective.tsp.base import TravelingSalesmanProblemObjectiveBase


class TravelingSalesmanProblemObjectiveDTO(TravelingSalesmanProblemObjectiveBase, ObjectiveDTO):
    distances: List[List[int]]
