from app.models.base_mapper import BaseMapper
from app.models.solver.ga.selection.tournament.mapper import TournamentSelectionMapper
from app.models.solver.ga.selection.tournament_nsga2.mapper import NSGA2basedTournamentSelectionMapper


class SelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "tournament": TournamentSelectionMapper,
        "tournament_nsga2": NSGA2basedTournamentSelectionMapper,
    }


    @staticmethod
    def get_mapper(selection_type: str) -> BaseMapper:
        return SelectionMapperRegistry._mapper_registry.get(selection_type)