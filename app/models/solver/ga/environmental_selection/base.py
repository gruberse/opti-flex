from abc import ABC
from typing import Literal

from pydantic import BaseModel


class EnvironmentalSelectionBase(ABC, BaseModel):
    environmental_selection_type: Literal['truncation', 'nsga2']