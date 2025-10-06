from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ElitistsEvaluationBase(ABC, BaseModel):
    fitness_evaluation_type: Literal['elitists'] = 'elitists'
    replace_offspring: bool