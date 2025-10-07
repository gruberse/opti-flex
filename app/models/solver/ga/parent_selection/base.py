from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ParentSelectionBase(ABC, BaseModel):
    parent_selection_type: Literal['tournament', 'tournament_nsga2']
