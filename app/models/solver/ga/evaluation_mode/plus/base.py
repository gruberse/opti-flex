from abc import ABC
from typing import Literal

from pydantic import BaseModel


class PlusModeBase(ABC, BaseModel):
    evaluation_mode_type: Literal['plus'] = 'plus'