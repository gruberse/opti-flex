from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedReductionBase(ABC, BaseModel):
    reduction_type: Literal['nsga2'] = 'nsga2'
