from app.models.base_mapper import BaseMapper
from app.models.solver.scipy_lsa.weight.dto import WeightDTO
from app.models.solver.scipy_lsa.weight.obj import Weight


class WeightMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: Weight) -> WeightDTO:
        return WeightDTO(
            objective_id=obj.objective_id,
            value=obj.value,
        )

    @staticmethod
    def from_dto(dto: WeightDTO) -> Weight:
        return Weight(
            objective_id=dto.objective_id,
            value=dto.value,
        )
