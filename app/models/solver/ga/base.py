from abc import ABC
from typing import Literal, Optional

from pydantic import BaseModel, model_validator

class GeneticAlgorithmBase(ABC, BaseModel):
    solver_type: Literal["ga"] = "ga"

    generations: int
    population_size: int

    re_evaluate_parents: bool = False

    random_seed: Optional[int] = None

    @model_validator(mode='after')
    def validate_setup(self):
        if self.population_size % 2 != 0:
            raise ValueError('Population size must be an even number')

        return self
