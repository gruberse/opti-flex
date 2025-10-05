from typing import List

from app.models.fitness.obj import Fitness
from .base import IndividualBase


class Individual(IndividualBase):
    encoding: List[int]
    fitness_list: List[Fitness] = []
