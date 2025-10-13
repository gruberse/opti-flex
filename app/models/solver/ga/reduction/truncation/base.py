from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TruncationReductionBase(ABC, BaseModel):
    reduction_type: Literal['truncation'] = 'truncation'