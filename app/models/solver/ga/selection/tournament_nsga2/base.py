from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedTournamentSelectionBase(ABC, BaseModel):
    selection_type: Literal['tournament_nsga2'] = 'tournament_nsga2'
    tournament_size: int = 2