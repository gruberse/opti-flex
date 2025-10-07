from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2ParentSelectionBase(ABC, BaseModel):
    parent_selection_type: Literal['nsga2'] = 'nsga2'
    tournament_size: int = 2