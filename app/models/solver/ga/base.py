from abc import ABC
from typing import Literal, Optional

from pydantic import BaseModel, model_validator

class GeneticAlgorithmBase(ABC, BaseModel):
    solver_type: Literal["ga"] = "ga"

    n_generations: int
    population_size: int
    n_parents: int

    random_seed: Optional[int] = None

    @model_validator(mode='after')
    def validate_setup(self):
        if self.population_size % 2 != 0:
            raise ValueError('population size must be an even number')

        return self
