from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.tournament_nsga2.dto import NSGA2basedTournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.obj import NSGA2basedTournamentSelection


class NSGA2basedTournamentSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: NSGA2basedTournamentSelection) -> NSGA2basedTournamentSelectionDTO:
        return NSGA2basedTournamentSelectionDTO(
            tournament_size=obj.tournament_size,
        )

    @staticmethod
    def from_dto(dto: NSGA2basedTournamentSelectionDTO) -> NSGA2basedTournamentSelection:
        return NSGA2basedTournamentSelection(
            tournament_size=dto.tournament_size,
        )