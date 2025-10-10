from abc import ABC
from typing import Literal

from pydantic import BaseModel


class CrossoverBase(ABC, BaseModel):
    crossover_type: Literal['pmx', 'ox', 'uox', 'cx', 'erx']
    crossover_probability: float
