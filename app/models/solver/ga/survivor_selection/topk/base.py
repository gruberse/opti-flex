from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TopKSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['topk'] = 'topk'