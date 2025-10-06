from abc import ABC
from typing import Literal

from pydantic import BaseModel


class FitnessEvaluationBase(ABC, BaseModel):
    fitness_evaluation_type: Literal['offspring', 'combined', 'elitists']