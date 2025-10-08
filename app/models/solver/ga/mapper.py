from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.registry import CrossoverMapperRegistry
from app.models.solver.ga.dto import GeneticAlgorithmDTO
from app.models.solver.ga.modification.registry import ModificationMapperRegistry
from app.models.solver.ga.mutation.registry import MutationMapperRegistry
from app.models.solver.ga.obj import GeneticAlgorithm
from app.models.solver.ga.parent_selection.registry import ParentSelectionMapperRegistry
from app.models.solver.ga.survivor_selection.registry import SurvivorSelectionMapperRegistry


class GeneticAlgorithmMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: GeneticAlgorithm) -> GeneticAlgorithmDTO:
        return GeneticAlgorithmDTO(
            generations=obj.generations,
            population_size=obj.population_size,
            parent_selection=ParentSelectionMapperRegistry.get_mapper(obj.parent_selection.parent_selection_type).to_dto(obj=obj.parent_selection),
            crossover=CrossoverMapperRegistry.get_mapper(obj.crossover.crossover_type).to_dto(obj=obj.crossover),
            mutation=MutationMapperRegistry.get_mapper(obj.mutation.mutation_type).to_dto(obj=obj.mutation),
            modification=ModificationMapperRegistry.get_mapper(obj.modification.modification_type).to_dto(obj=obj.modification),
            survivor_selection=SurvivorSelectionMapperRegistry.get_mapper(obj.survivor_selection.survivor_selection_type).to_dto(obj=obj.survivor_selection),
            random_seed=obj.random_seed,
        )

    @staticmethod
    def from_dto(dto: GeneticAlgorithmDTO) -> GeneticAlgorithm:
        return GeneticAlgorithm(
            generations=dto.generations,
            population_size=dto.population_size,
            parent_selection=ParentSelectionMapperRegistry.get_mapper(dto.parent_selection.parent_selection_type).from_dto(dto=dto.parent_selection),
            crossover=CrossoverMapperRegistry.get_mapper(dto.crossover.crossover_type).from_dto(dto=dto.crossover),
            mutation=MutationMapperRegistry.get_mapper(dto.mutation.mutation_type).from_dto(dto=dto.mutation),
            modification=ModificationMapperRegistry.get_mapper(dto.modification.modification_type).from_dto(dto=dto.modification),
            survivor_selection=SurvivorSelectionMapperRegistry.get_mapper(dto.survivor_selection.survivor_selection_type).from_dto(dto=dto.survivor_selection),
            random_seed=dto.random_seed,
        )
