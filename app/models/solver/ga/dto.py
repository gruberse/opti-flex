from typing import Union

from app.models.solver.dto import SolverDTO
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.pmx.dto import PartiallyMatchedCrossoverDTO
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.modification.append_parents.dto import AppendParentsModificationDTO
from app.models.solver.ga.modification.inject_elitists.dto import InjectElitistsModificationDTO
from app.models.solver.ga.modification.none.dto import NoneModificationDTO
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.parent_selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.dto import NSGA2BasedTournamentSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2BasedSurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.topk.dto import TopKSurvivalSelectionDTO


class GeneticAlgorithmDTO(GeneticAlgorithmBase, SolverDTO):
    parent_selection: Union[TournamentSelectionDTO, NSGA2BasedTournamentSelectionDTO]
    crossover: Union[OrderCrossoverDTO, PartiallyMatchedCrossoverDTO, UniformOrderBasedCrossoverDTO, CycleCrossoverDTO]
    mutation: Union[InversionMutationDTO, InsertMutationDTO, ScrambleMutationDTO, ShiftMutationDTO, SwapMutationDTO]
    modification: Union[NoneModificationDTO, AppendParentsModificationDTO, InjectElitistsModificationDTO]
    survivor_selection: Union[TopKSurvivalSelectionDTO, NSGA2BasedSurvivalSelectionDTO]
