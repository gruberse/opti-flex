import numpy as np

from app.models.base_mapper import BaseMapper
from app.models.obfuscation.registry import ObfuscationMapperRegistry
from app.models.objective.tsp.dto import TravelingSalesmanProblemObjectiveDTO
from app.models.objective.tsp.obj import TravelingSalesmanProblemObjective


class TravelingSalesmanProblemObjectiveMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TravelingSalesmanProblemObjective) -> TravelingSalesmanProblemObjectiveDTO:
        obfuscation = None
        if obj.obfuscation:
            obfuscation = (ObfuscationMapperRegistry.get_mapper(obj.obfuscation.obfuscation_type)
                           .to_dto(obj=obj.obfuscation))

        return TravelingSalesmanProblemObjectiveDTO(
            objective_id=obj.objective_id,
            distances=obj.matrix.tolist(),
            obfuscation=obfuscation,
            privacy_engine=obj.privacy_engine,
            encoding_url=obj.encoding_url,
        )

    @staticmethod
    def from_dto(dto: TravelingSalesmanProblemObjectiveDTO) -> TravelingSalesmanProblemObjective:
        obfuscation = None
        if dto.obfuscation:
            obfuscation = (ObfuscationMapperRegistry.get_mapper(dto.obfuscation.obfuscation_type)
                           .from_dto(dto=dto.obfuscation))

        return TravelingSalesmanProblemObjective(
            objective_id=dto.objective_id,
            matrix=np.array(dto.distances, dtype=np.int64),
            obfuscation=obfuscation,
            privacy_engine=dto.privacy_engine,
            encoding_url = dto.encoding_url,
        )
