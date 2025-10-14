from .base import FitnessBase


class Fitness(FitnessBase):

    def get_estimated_or_actual_fitness(self) -> int:
        if isinstance(self.estimated_fitness, int):
            return self.estimated_fitness
        return self.actual_fitness


def test():
    fitness = Fitness(objective_id='test', actual_fitness=0)
    assert fitness.get_estimated_or_actual_fitness() == 0

    fitness = Fitness(objective_id='test', actual_fitness=0, estimated_fitness=None)
    assert fitness.get_estimated_or_actual_fitness() == 0

    fitness = Fitness(objective_id='test', actual_fitness=0, estimated_fitness=1)
    assert fitness.get_estimated_or_actual_fitness() == 1

    fitness = Fitness(objective_id='test', actual_fitness=None, estimated_fitness=1)
    assert fitness.get_estimated_or_actual_fitness() == 1

    fitness = Fitness(objective_id='test', estimated_fitness=1)
    assert fitness.get_estimated_or_actual_fitness() == 1
