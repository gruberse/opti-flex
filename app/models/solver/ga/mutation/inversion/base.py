from abc import ABC
from typing import Literal

from pydantic import BaseModel


class InversionMutationBase(ABC, BaseModel):
    mutation_type: Literal['inversion'] = 'inversion'