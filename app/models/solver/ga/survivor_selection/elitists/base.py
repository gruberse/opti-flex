from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ElitistsSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['elitists'] = 'elitists'