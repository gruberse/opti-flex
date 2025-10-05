from app.models.base_mapper import BaseMapper

from app.models.solver.scipy_lsa.weight.mapper import WeightMapper
from app.models.solver.scipy_lsa.weights.dto import WeightsDTO
from app.models.solver.scipy_lsa.weights.obj import Weights


class WeightsMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: Weights) -> WeightsDTO:
        weight_list = [WeightMapper.to_dto(weight) for weight in obj.weight_list]

        return WeightsDTO(
            weight_list=weight_list,
        )

    @staticmethod
    def from_dto(dto: WeightsDTO) -> Weights:
        weight_list = [WeightMapper.from_dto(weight) for weight in dto.weight_list]

        return Weights(
            weight_list=weight_list,
        )
