from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TruncationSurvivalBase(ABC, BaseModel):
    survival_type: Literal['truncation'] = 'truncation'