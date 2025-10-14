from abc import ABC
from typing import Literal

from pydantic import BaseModel


class NSGA2basedSurvivalBase(ABC, BaseModel):
    survival_type: Literal['nsga2'] = 'nsga2'
