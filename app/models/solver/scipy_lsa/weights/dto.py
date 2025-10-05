from typing import List

from app.models.solver.scipy_lsa.weight.dto import WeightDTO
from app.models.solver.scipy_lsa.weights.base import WeightsBase


class WeightsDTO(WeightsBase):
    weight_list: List[WeightDTO]
