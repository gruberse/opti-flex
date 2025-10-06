from abc import ABC
from typing import Literal

from pydantic import BaseModel


class OffspringEvaluationBase(ABC, BaseModel):
    fitness_evaluation_type: Literal['offspring'] = 'offspring'