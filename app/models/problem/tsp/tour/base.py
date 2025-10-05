from abc import ABC
from typing import List

from pydantic import BaseModel


class TourBase(ABC, BaseModel):
    cities: List[int]
