from abc import ABC

from pydantic import BaseModel


class WeightBase(ABC, BaseModel):
    objective_id: str
    value: float
