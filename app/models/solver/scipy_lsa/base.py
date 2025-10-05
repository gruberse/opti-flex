from abc import ABC
from typing import Literal

from pydantic import BaseModel


class ScipyLinearSumAssignmentBase(ABC, BaseModel):
    solver_type: Literal["scipy_lsa"] = "scipy_lsa"
    maximize: bool = True
