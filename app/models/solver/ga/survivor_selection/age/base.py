from abc import ABC
from typing import Literal

from pydantic import BaseModel


class AgeBasedSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['age'] = 'age'