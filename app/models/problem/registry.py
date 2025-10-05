from .ap.mapper import AssignmentProblemMapper
from .problem_mapper import ProblemMapper
from .tsp.mapper import TravelingSalesmanProblemMapper


class ProblemMapperRegistry:
    _mapper_registry: dict[str, ProblemMapper] = {
        "tsp": TravelingSalesmanProblemMapper,
        "ap": AssignmentProblemMapper
    }

    @staticmethod
    def get_mapper(problem_type: str) -> ProblemMapper:
        return ProblemMapperRegistry._mapper_registry.get(problem_type)
