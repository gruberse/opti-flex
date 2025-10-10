from abc import ABC
from typing import Literal

from pydantic import BaseModel


class EdgeRecombinationCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['erx'] = 'erx'