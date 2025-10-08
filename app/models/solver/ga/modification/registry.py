from app.models.base_mapper import BaseMapper
from app.models.solver.ga.modification.append_parents.mapper import AppendParentsModificationMapper
from app.models.solver.ga.modification.inject_elitists.mapper import InjectElitistsModificationMapper
from app.models.solver.ga.modification.none.mapper import NoneModificationMapper


class ModificationMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "none": NoneModificationMapper,
        "append_parents": AppendParentsModificationMapper,
        "inject_elitists": InjectElitistsModificationMapper
    }


    @staticmethod
    def get_mapper(survivor_selection_type: str) -> BaseMapper:
        return ModificationMapperRegistry._mapper_registry.get(survivor_selection_type)