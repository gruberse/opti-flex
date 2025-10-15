from app.models.base_mapper import BaseMapper
from app.models.solver.ga.crossover.registry import CrossoverMapperRegistry
from app.models.solver.ga.dto import GeneticAlgorithmDTO
from app.models.solver.ga.mutation.registry import MutationMapperRegistry
from app.models.solver.ga.obj import GeneticAlgorithm
from app.models.solver.ga.selection.registry import SelectionMapperRegistry
from app.models.solver.ga.survival.registry import SurvivalMapperRegistry


class GeneticAlgorithmMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: GeneticAlgorithm) -> GeneticAlgorithmDTO:
        return GeneticAlgorithmDTO(
            n_generations=obj.n_generations,
            population_size=obj.population_size,
            n_elitists=obj.n_elitists,
            combine_populations=obj.combine_populations,
            selection=SelectionMapperRegistry.get_mapper(obj.selection.selection_type).to_dto(obj=obj.selection),
            crossover=CrossoverMapperRegistry.get_mapper(obj.crossover.crossover_type).to_dto(obj=obj.crossover),
            mutation=MutationMapperRegistry.get_mapper(obj.mutation.mutation_type).to_dto(obj=obj.mutation),
            survival=SurvivalMapperRegistry.get_mapper(obj.survival.survival_type).to_dto(obj=obj.survival),
            random_seed=obj.random_seed,
        )

    @staticmethod
    def from_dto(dto: GeneticAlgorithmDTO) -> GeneticAlgorithm:
        return GeneticAlgorithm(
            n_generations=dto.n_generations,
            population_size=dto.population_size,
            n_elitists=dto.n_elitists,
            combine_populations=dto.combine_populations,
            selection=SelectionMapperRegistry.get_mapper(dto.selection.selection_type).from_dto(dto=dto.selection),
            crossover=CrossoverMapperRegistry.get_mapper(dto.crossover.crossover_type).from_dto(dto=dto.crossover),
            mutation=MutationMapperRegistry.get_mapper(dto.mutation.mutation_type).from_dto(dto=dto.mutation),
            survival=SurvivalMapperRegistry.get_mapper(dto.survival.survival_type).from_dto(dto=dto.survival),
            random_seed=dto.random_seed,
        )
