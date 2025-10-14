from typing import Optional, List

from app.models.individual.obj import Individual


class NSGA2Individual(Individual):
    domination_count: int = 0
    dominated_individuals: List = []
    rank: Optional[int] = None
    crowding_distance: float = 0.0

    def to_individual(self) -> Individual:
        return Individual(
            encoding=self.encoding,
            fitness_list=self.fitness_list,
        )
