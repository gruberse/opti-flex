from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedTournamentSelectionBase(ABC, BaseModel):
    parent_selection_type: Literal['nsga2_tournament'] = 'nsga2_tournament'
    tournament_size: int = 2