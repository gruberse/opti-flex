from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TournamentSelectionBase(ABC, BaseModel):
    selection_type: Literal['tournament'] = 'tournament'
    tournament_size: int
