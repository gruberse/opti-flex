from app.models.base_mapper import BaseMapper
from app.models.solver.ga.mutation.insert.mapper import InsertMutationMapper
from app.models.solver.ga.mutation.inversion.mapper import InversionMutationMapper
from app.models.solver.ga.mutation.scramble.mapper import ScrambleMutationMapper
from app.models.solver.ga.mutation.shift.mapper import ShiftMutationMapper
from app.models.solver.ga.mutation.swap.mapper import SwapMutationMapper


class MutationMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "inversion": InversionMutationMapper,
        "scramble": ScrambleMutationMapper,
        "shift": ShiftMutationMapper,
        "swap": SwapMutationMapper,
        "insert": InsertMutationMapper,
    }


    @staticmethod
    def get_mapper(mutation_type: str) -> BaseMapper:
        return MutationMapperRegistry._mapper_registry.get(mutation_type)