from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.tournament.mapper import TournamentSelectionMapper
from app.models.solver.ga.parent_selection.tournament_nsga2.mapper import NSGA2basedTournamentSelectionMapper


class ParentSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "tournament": TournamentSelectionMapper,
        "nsga2_tournament": NSGA2basedTournamentSelectionMapper,
    }


    @staticmethod
    def get_mapper(parent_selection_type: str) -> BaseMapper:
        return ParentSelectionMapperRegistry._mapper_registry.get(parent_selection_type)