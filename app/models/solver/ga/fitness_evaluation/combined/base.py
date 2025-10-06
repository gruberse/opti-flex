from abc import ABC

from pydantic import BaseModel
from typing_extensions import Literal


class CombinedEvaluationBase(ABC, BaseModel):
    fitness_evaluation_type: Literal['combined'] = 'combined'