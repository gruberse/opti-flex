from abc import ABC
from typing import Literal

from pydantic import BaseModel


class SwapMutationBase(ABC, BaseModel):
    mutation_type: Literal['swap'] = 'swap'