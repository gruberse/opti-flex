from abc import ABC
from typing import Literal, Optional

from pydantic import BaseModel, model_validator


class GeneticAlgorithmBase(ABC, BaseModel):
    solver_type: Literal["ga"] = "ga"

    n_generations: int
    population_size: int

    n_elitists: int = 0

    re_evaluate_previous_population: bool = False

    random_seed: Optional[int] = None

    @model_validator(mode="after")
    def check_init(self):
        if self.n_elitists > 0 and self.re_evaluate_previous_population == True:
            raise ValueError("elitism and re-evaluation of previous population cannot be used at the same time")
        return self