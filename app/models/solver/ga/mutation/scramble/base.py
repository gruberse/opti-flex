from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ScrambleMutationBase(ABC, BaseModel):
    mutation_type: Literal['scramble'] = 'scramble'