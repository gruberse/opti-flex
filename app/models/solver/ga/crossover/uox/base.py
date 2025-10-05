from abc import ABC
from typing import Literal

from pydantic import BaseModel


class UniformOrderBasedCrossoverBase(ABC, BaseModel):
    crossover_type: Literal['uox'] = 'uox'
    keep_genes_probability: float
