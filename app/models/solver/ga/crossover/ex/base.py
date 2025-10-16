from abc import ABC
from typing import Literal

from pydantic import BaseModel


class EdgeCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['ex'] = 'ex'