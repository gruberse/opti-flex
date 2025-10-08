from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.modification.none.dto import NoneModificationDTO
from app.models.solver.ga.modification.none.obj import NoneModification


class NoneModificationMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NoneModification) -> NoneModificationDTO:
        return NoneModificationDTO()

    @staticmethod
    def from_dto(dto: NoneModificationDTO) -> NoneModification:
        return NoneModification()
