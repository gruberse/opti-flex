from typing import List

from app.models.fitness.dto import FitnessDTO
from .base import IndividualBase


class IndividualDTO(IndividualBase):
    fitness_list: List[FitnessDTO] = []
