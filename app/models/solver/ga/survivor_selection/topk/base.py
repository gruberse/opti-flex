from abc import ABC
from typing import Literal

from pydantic import BaseModel


class TopKSurvivalSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['topk'] = 'topk'