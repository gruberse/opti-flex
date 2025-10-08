from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NoneModificationBase(ABC, BaseModel):
    modification_type: Literal['none'] = 'none'
