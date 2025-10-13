from abc import ABC
from typing import Literal

from pydantic import BaseModel


class SelectionBase(ABC, BaseModel):
    selection_type: Literal['tournament', 'tournament_nsga2']
