from typing import List

from .base import PopulationBase
from ..individual.dto import IndividualDTO


class PopulationDTO(PopulationBase):
    individuals: List[IndividualDTO] = []
    non_dominated_individuals: List[IndividualDTO] = []
