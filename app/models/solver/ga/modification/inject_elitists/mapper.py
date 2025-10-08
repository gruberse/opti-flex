from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.modification.inject_elitists.dto import InjectElitistsModificationDTO
from app.models.solver.ga.modification.inject_elitists.obj import InjectElitistsModification


class InjectElitistsModificationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: InjectElitistsModification) -> InjectElitistsModificationDTO:
        return InjectElitistsModificationDTO()

    @staticmethod
    def from_dto(dto: InjectElitistsModificationDTO) -> InjectElitistsModification:
        return InjectElitistsModification()
