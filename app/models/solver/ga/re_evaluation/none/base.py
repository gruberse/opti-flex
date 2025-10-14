from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NoReEvaluationBase(ABC, BaseModel):
    re_evaluation_type: Literal['none'] = 'none'
