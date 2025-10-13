from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedSurvivorSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['nsga2'] = 'nsga2'
