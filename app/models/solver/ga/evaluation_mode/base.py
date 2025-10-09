from abc import ABC
from typing import Literal

from pydantic import BaseModel


class EvaluationModeBase(ABC, BaseModel):
    evaluation_mode_type: Literal['comma', 'plus', 'plus_elitists']