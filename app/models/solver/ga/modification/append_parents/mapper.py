from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.modification.append_parents.dto import AppendParentsModificationDTO
from app.models.solver.ga.modification.append_parents.obj import AppendParentsModification


class AppendParentsModificationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: AppendParentsModification) -> AppendParentsModificationDTO:
        return AppendParentsModificationDTO()


    @staticmethod
    def from_dto(dto: AppendParentsModificationDTO) -> AppendParentsModification:
        return AppendParentsModification()
