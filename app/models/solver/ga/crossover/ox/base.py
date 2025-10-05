from abc import ABC
from typing import Literal

from pydantic import BaseModel


class OrderCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['ox'] = 'ox'