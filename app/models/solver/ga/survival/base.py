from abc import ABC
from typing import Literal

from pydantic import BaseModel


class SurvivalBase(ABC, BaseModel):
    survival_type: Literal['truncation', 'nsga2']