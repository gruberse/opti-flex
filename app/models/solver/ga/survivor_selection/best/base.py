from abc import ABC
from typing import Literal

from pydantic import BaseModel


class BestIndividualsSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['best'] = 'best'