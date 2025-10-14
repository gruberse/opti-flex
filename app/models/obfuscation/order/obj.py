from typing import Dict, List

from app.models.fitness.obj import Fitness
from app.models.obfuscation.obj import Obfuscation
from .base import OrderObfuscationBase
from ...individual.obj import Individual


class OrderObfuscation(OrderObfuscationBase, Obfuscation):
    endpoint_privacy_engine: str = 'computePopulationOrder'

    def obfuscate_and_estimate(self, fitness_list: List[Fitness]) -> List[Fitness]:
        fitness_values = [fitness.actual_fitness for fitness in fitness_list]

        maximum_fitness = max(fitness_values)
        estimated_min_fitness = maximum_fitness - (2 * abs(maximum_fitness))
        distance = abs((maximum_fitness - estimated_min_fitness) / (len(fitness_list) - 1)) if len(fitness_list) > 1 else 0

        fitness_values.sort(reverse=True)
        number_of_fitness_values = len(fitness_values)

        used_indices: List = []
        for fitness in fitness_list:
            idx = number_of_fitness_values - 1 - fitness_values[::-1].index(fitness.actual_fitness)

            while idx in used_indices:
                idx -= 1

            fitness.estimated_fitness = round(maximum_fitness - (idx * distance))
            used_indices.append(idx)

        return fitness_list

    def estimate_based_on_privacy_engine(self, objective_id: str, individuals: List[Individual], response: Dict) -> List[Fitness]:
        fitness_list = []

        max_fitness = response['maximum']
        order = response['order'][::-1]

        estimated_min_fitness = max_fitness - (2 * abs(max_fitness))
        distance = abs((max_fitness - estimated_min_fitness) / (len(individuals) - 1)) if len(individuals) > 1 else 0

        for i in range(len(individuals)):
            estimated_fitness = round(max_fitness - (distance * order.index(i)))
            fitness_list.append(Fitness(objective_id=objective_id, estimated_fitness=estimated_fitness))

        return fitness_list


def test():
    obfuscation = OrderObfuscation()

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
    assert estimated_fitness_list[1].estimated_fitness == 80
    assert estimated_fitness_list[2].estimated_fitness == 60
    assert estimated_fitness_list[3].estimated_fitness == 20
    assert estimated_fitness_list[4].estimated_fitness == 40
    assert estimated_fitness_list[5].estimated_fitness == 0
    assert estimated_fitness_list[6].estimated_fitness == -40
    assert estimated_fitness_list[7].estimated_fitness == -20
    assert estimated_fitness_list[8].estimated_fitness == -60
    assert estimated_fitness_list[9].estimated_fitness == -80
    assert estimated_fitness_list[10].estimated_fitness == -100