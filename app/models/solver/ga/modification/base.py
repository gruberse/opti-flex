from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ModificationBase(ABC, BaseModel):
    modification_type: Literal['none', 'append_parents', 'inject_elitists']