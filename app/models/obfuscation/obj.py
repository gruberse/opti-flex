from abc import abstractmethod, ABC
from typing import Dict, List

from app.models.fitness.obj import Fitness
from .base import ObfuscationBase
from ..individual.obj import Individual


class Obfuscation(ObfuscationBase, ABC):

    @abstractmethod
    def obfuscate_and_estimate(self, fitness_list: List[Fitness]) -> List[Fitness]:
        pass

    @abstractmethod
    def estimate_based_on_privacy_engine(self, objective_id: str, individuals: List[Individual], response: Dict) -> List[Fitness]:
        pass
