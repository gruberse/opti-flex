from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ElitistsReEvaluationBase(ABC, BaseModel):
    re_evaluation_type: Literal['elitists'] = 'elitists'
    n_elitists: int = 0
