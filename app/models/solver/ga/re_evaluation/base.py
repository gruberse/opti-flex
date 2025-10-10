from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ReEvaluationBase(ABC, BaseModel):
    re_evaluation_type: Literal['population', 'elitists']