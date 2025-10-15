from abc import ABC
from typing import Literal, Optional

from pydantic import BaseModel, model_validator


class GeneticAlgorithmBase(ABC, BaseModel):
    solver_type: Literal["ga"] = "ga"

    n_generations: int
    population_size: int

    n_elitists: int = 0

    combine_populations: bool = False

    random_seed: Optional[int] = None

    @model_validator(mode="after")
    def check_init(self):
        if self.n_elitists > 0 and self.combine_populations == True:
            raise ValueError("elitism and combination with the last population cannot be used at the same time")
        return self