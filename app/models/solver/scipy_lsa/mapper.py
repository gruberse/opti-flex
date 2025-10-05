from app.models.base_mapper import BaseMapper

from .dto import ScipyLinearSumAssignmentDTO
from .obj import ScipyLinearSumAssignment
from .weights.mapper import WeightsMapper


class ScipyLinearSumAssignmentMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: ScipyLinearSumAssignment) -> ScipyLinearSumAssignmentDTO:
        weights_list = None
        if obj.weights_list:
            weights_list = [WeightsMapper.to_dto(weights) for weights in obj.weights_list]

        return ScipyLinearSumAssignmentDTO(
            weights_list=weights_list,
            maximize=obj.maximize,
        )

    @staticmethod
    def from_dto(dto: ScipyLinearSumAssignmentDTO) -> ScipyLinearSumAssignment:
        weightings = None
        if dto.weights_list:
            weightings = [WeightsMapper.from_dto(weights) for weights in dto.weights_list]

        return ScipyLinearSumAssignment(
            weights_list=weightings,
            maximize=dto.maximize,
        )
