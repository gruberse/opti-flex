from abc import ABC
from typing import Literal

from pydantic import BaseModel


class CommaModeBase(ABC, BaseModel):
    evaluation_mode_type: Literal['comma'] = 'comma'
