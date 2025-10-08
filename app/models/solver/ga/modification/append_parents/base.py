from abc import ABC
from typing import Literal

from pydantic import BaseModel


class AppendParentsModificationBase(ABC, BaseModel):
    modification_type: Literal['append_parents'] = 'append_parents'