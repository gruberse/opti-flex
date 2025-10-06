from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedElitistsSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['nsga2_elitists'] = 'nsga2_elitists'
