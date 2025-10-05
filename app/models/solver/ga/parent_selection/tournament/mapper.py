from app.models.base_mapper import BaseMapper
from app.models.solver.ga.parent_selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament.obj import TournamentSelection


class TournamentSelectionMapper(BaseMapper):
    @staticmethod
    def to_dto(obj: TournamentSelection) -> TournamentSelectionDTO:
        return TournamentSelectionDTO(
            tournament_size=obj.tournament_size,
        )


    @staticmethod
    def from_dto(dto: TournamentSelectionDTO) -> TournamentSelection:
        return TournamentSelection(
            tournament_size=dto.tournament_size,
        )
