from typing import Any

from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.tournament_nsga2.dto import NSGA2BasedTournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.obj import NSGA2BasedTournamentSelection


class NSGA2basedTournamentSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2BasedTournamentSelection) -> NSGA2BasedTournamentSelectionDTO:
        return NSGA2BasedTournamentSelectionDTO(
            tournament_size=obj.tournament_size,
        )

    @staticmethod
    def from_dto(dto: NSGA2BasedTournamentSelectionDTO) -> NSGA2BasedTournamentSelection:
        return NSGA2BasedTournamentSelection(
            tournament_size=dto.tournament_size,
        )