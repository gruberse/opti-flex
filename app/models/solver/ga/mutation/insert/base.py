from abc import ABC
from typing import Literal

from pydantic import BaseModel


class InsertMutationBase(ABC, BaseModel):
    mutation_type: Literal['insert'] = 'insert'