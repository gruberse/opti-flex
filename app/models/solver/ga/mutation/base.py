from abc import ABC
from typing import Literal

from pydantic import BaseModel


class MutationBase(ABC, BaseModel):
    mutation_type: Literal['inversion', 'scramble', 'shift', 'swap', 'insert']
    mutation_probability: float
