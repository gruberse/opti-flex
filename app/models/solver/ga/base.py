from abc import ABC
from typing import Literal, Optional

from pydantic import BaseModel, model_validator

class GeneticAlgorithmBase(ABC, BaseModel):
    solver_type: Literal["ga"] = "ga"

    n_generations: int
    population_size: int
    n_parents: int

    random_seed: Optional[int] = None
