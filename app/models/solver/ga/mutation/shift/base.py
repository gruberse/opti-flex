from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ShiftMutationBase(ABC, BaseModel):
    mutation_type: Literal['shift'] = 'shift'