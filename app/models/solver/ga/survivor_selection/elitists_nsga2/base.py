from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedElitistsSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['elitists_nsga2'] = 'elitists_nsga2'
