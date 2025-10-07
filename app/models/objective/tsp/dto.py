from typing import List

from app.models.objective.dto import ObjectiveDTO
from app.models.objective.tsp.base import TravelingSalesmanObjectiveBase


class TravelingSalesmanObjectiveDTO(TravelingSalesmanObjectiveBase, ObjectiveDTO):
    distances: List[List[int]]
