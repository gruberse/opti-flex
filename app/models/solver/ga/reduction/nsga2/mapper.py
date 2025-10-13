from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.reduction.nsga2.dto import NSGA2BasedReductionDTO
from app.models.solver.ga.reduction.nsga2.obj import NSGA2BasedReduction


class NSGA2basedReductionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2BasedReduction) -> NSGA2BasedReductionDTO:
        return NSGA2BasedReductionDTO()


    @staticmethod
    def from_dto(dto: NSGA2BasedReductionDTO) -> NSGA2BasedReduction:
        return NSGA2BasedReduction()