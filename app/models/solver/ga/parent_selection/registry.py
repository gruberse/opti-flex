import enum

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.nsga2_tournament.mapper import NSGA2BasedTournamentSelectionMapper
from app.models.solver.ga.parent_selection.tournament.mapper import TournamentSelectionMapper


class ParentSelectionMapperRegistry:
    _mapper_registry: dict[str, BaseMapper] = {
        "tournament": TournamentSelectionMapper,
        "nsga2_tournament": NSGA2BasedTournamentSelectionMapper,
    }


    @staticmethod
    def get_mapper(parent_selection_type: str) -> BaseMapper:
        return ParentSelectionMapperRegistry._mapper_registry.get(parent_selection_type)