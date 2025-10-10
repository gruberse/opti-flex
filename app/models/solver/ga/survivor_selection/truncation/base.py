from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TruncationSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['truncation'] = 'truncation'