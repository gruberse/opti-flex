from abc import ABC
from typing import Literal

from pydantic import BaseModel


class SolverBase(ABC, BaseModel):
    solver_type: Literal["scipy_lsa", "ga"]
