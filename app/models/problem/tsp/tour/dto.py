from typing import List

from app.models.fitness.dto import FitnessDTO
from app.models.problem.tsp.tour.base import TourBase


class TourDTO(TourBase):
    fitness_list: List[FitnessDTO]
