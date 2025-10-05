from abc import ABC
from typing import Literal

from pydantic import BaseModel


class SurvivorSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['age_based', 'nsga2']