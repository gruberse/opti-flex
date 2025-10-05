from typing import List

from app.models.fitness.obj import Fitness
from app.models.problem.tsp.tour.base import TourBase


class Tour(TourBase):
    fitness_list: List[Fitness]
