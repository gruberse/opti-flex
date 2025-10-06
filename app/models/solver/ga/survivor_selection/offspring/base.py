from abc import ABC
from typing import Literal

from pydantic import BaseModel


class OffspringSelectionBase(ABC, BaseModel):
    survivor_selection_type: Literal['offspring'] = 'offspring'