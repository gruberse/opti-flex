import numpy as np

from app.models.base_mapper import BaseMapper
from app.models.obfuscation.registry import ObfuscationMapperRegistry
from .dto import AssignmentProblemObjectiveDTO
from .obj import AssignmentProblemObjective


class AssignmentProblemObjectiveMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: AssignmentProblemObjective) -> AssignmentProblemObjectiveDTO:
        obfuscation = None
        if obj.obfuscation:
            obfuscation = (ObfuscationMapperRegistry.get_mapper(obj.obfuscation.obfuscation_type)
                           .to_dto(obj=obj.obfuscation))

        return AssignmentProblemObjectiveDTO(
            objective_id=obj.objective_id,
            weights=obj.matrix.tolist(),
            obfuscation=obfuscation,
            privacy_engine=obj.privacy_engine,
            encoding_url=obj.encoding_url,
        )

    @staticmethod
    def from_dto(dto: AssignmentProblemObjectiveDTO) -> AssignmentProblemObjective:
        obfuscation = None
        if dto.obfuscation:
            obfuscation = (ObfuscationMapperRegistry.get_mapper(dto.obfuscation.obfuscation_type)
                           .from_dto(dto=dto.obfuscation))

        return AssignmentProblemObjective(
            objective_id=dto.objective_id,
            matrix=np.array(dto.weights, dtype=np.int64),
            obfuscation=obfuscation,
            privacy_engine=dto.privacy_engine,
            encoding_url=dto.encoding_url,
        )
