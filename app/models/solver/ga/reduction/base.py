from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ReductionBase(ABC, BaseModel):
    reduction_type: Literal['truncation', 'nsga2']