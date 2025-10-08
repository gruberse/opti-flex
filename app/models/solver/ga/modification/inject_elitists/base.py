from abc import ABC
from typing import Literal

from pydantic import BaseModel


class InjectElitistsModificationBase(ABC, BaseModel):
    modification_type: Literal['inject_elitists'] = 'inject_elitists'
