from typing import Dict, List

from app.models.fitness.obj import Fitness
from app.models.obfuscation.obj import Obfuscation
from app.models.population.obj import Population
from .base import TopObfuscationBase
from ...individual.obj import Individual


class TopObfuscation(TopObfuscationBase, Obfuscation):
    endpoint_privacy_engine: str = ''

    def __init__(self, /, **data):
        super().__init__(**data)
        self.endpoint_privacy_engine = f'computeTopIndividuals/{self.top}'

    def obfuscate_and_estimate(self, fitness_list: List[Fitness]) -> List[Fitness]:
        fitness_values = [fitness.actual_fitness for fitness in fitness_list]

        maximum_fitness = max(fitness_values)
        estimated_min_fitness = maximum_fitness - (2 * abs(maximum_fitness))

        indices_top_n_individuals = sorted(
            range(len(fitness_values)), # Create a list of indices
            key=lambda i: (fitness_values[i], i), # sort by fitness value and then by index
            reverse=True # sort in descending order
        )[:self.top]

        for i, fitness in enumerate(fitness_list):
            fitness.estimated_fitness = maximum_fitness if i in indices_top_n_individuals else estimated_min_fitness

        return fitness_list

    def estimate_based_on_privacy_engine(self, objective_id: str, individuals: List[Individual], response: Dict) -> List[Fitness]:
        fitness_list = []

        maximum_fitness = response['highest']
        indices_top_individuals = response['indices']

        estimated_min_fitness = maximum_fitness - (2 * abs(maximum_fitness))

        for i in range(len(individuals)):
            estimated_fitness = maximum_fitness if i in indices_top_individuals else estimated_min_fitness
            fitness_list.append(Fitness(objective_id=objective_id, estimated_fitness=estimated_fitness))

        return fitness_list

def test():
    obfuscation = TopObfuscation(top=4)

    fitness_list = [
        Fitness(objective_id="test", actual_fitness=100),
        Fitness(objective_id="test", actual_fitness=90),
        Fitness(objective_id="test", actual_fitness=80),
        Fitness(objective_id="test", actual_fitness=70),
        Fitness(objective_id="test", actual_fitness=70),
        Fitness(objective_id="test", actual_fitness=65),
        Fitness(objective_id="test", actual_fitness=30),
        Fitness(objective_id="test", actual_fitness=30),
        Fitness(objective_id="test", actual_fitness=20),
        Fitness(objective_id="test", actual_fitness=10),
        Fitness(objective_id="test", actual_fitness=0),
    ]

    estimated_fitness_list = obfuscation.obfuscate_and_estimate(fitness_list)

    assert estimated_fitness_list[0].estimated_fitness == 100
    assert estimated_fitness_list[1].estimated_fitness == 100
    assert estimated_fitness_list[2].estimated_fitness == 100
    assert estimated_fitness_list[3].estimated_fitness == -100
    assert estimated_fitness_list[4].estimated_fitness == 100
    assert estimated_fitness_list[5].estimated_fitness == -100
    assert estimated_fitness_list[6].estimated_fitness == -100
    assert estimated_fitness_list[7].estimated_fitness == -100
    assert estimated_fitness_list[8].estimated_fitness == -100
    assert estimated_fitness_list[9].estimated_fitness == -100
    assert estimated_fitness_list[10].estimated_fitness == -100