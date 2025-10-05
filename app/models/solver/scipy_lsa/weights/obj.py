from typing import List

from app.models.solver.scipy_lsa.weight.obj import Weight
from app.models.solver.scipy_lsa.weights.base import WeightsBase


class Weights(WeightsBase):
    weight_list: List[Weight]
