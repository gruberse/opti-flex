from abc import ABC
from typing import Literal

from pydantic import BaseModel


class GenerationalSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['generational'] = 'generational'