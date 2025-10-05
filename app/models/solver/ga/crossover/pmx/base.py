from abc import ABC
from typing import Literal

from pydantic import BaseModel


class PartiallyMatchedCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['pmx'] = 'pmx'
