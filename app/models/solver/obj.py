import multiprocessing
from abc import abstractmethod
from typing import List

from .base import SolverBase
from ..problem.obj import Problem


class Solver(SolverBase):
    @abstractmethod
    def solve(self, problem: Problem, population_queue: multiprocessing.Queue, populations: List) -> None:
        pass
