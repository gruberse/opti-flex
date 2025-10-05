from abc import ABC
from typing import Literal

from pydantic import BaseModel


class CycleCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['cx'] = 'cx'