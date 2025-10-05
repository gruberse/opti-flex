from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.nsga2_tournament.dto import NSGA2TournamentSelectionDTO
from app.models.solver.ga.parent_selection.nsga2_tournament.obj import NSGA2TournamentSelection


class NSGA2TournamentSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2TournamentSelection) -> NSGA2TournamentSelectionDTO:
        return NSGA2TournamentSelectionDTO(
            tournament_size=obj.tournament_size,
        )

    @staticmethod
    def from_dto(dto: NSGA2TournamentSelectionDTO) -> NSGA2TournamentSelection:
        return NSGA2TournamentSelection(
            tournament_size=dto.tournament_size,
        )