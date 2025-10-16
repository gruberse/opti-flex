from typing import Union

from app.models.solver.dto import SolverDTO
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.ex.dto import EdgeCrossoverDTO
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.pmx.dto import PartiallyMappedCrossoverDTO
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.selection.tournament_nsga2.dto import NSGA2basedTournamentSelectionDTO
from app.models.solver.ga.survival.nsga2.dto import NSGA2basedSurvivalDTO
from app.models.solver.ga.survival.truncation.dto import TruncationSurvivalDTO


class GeneticAlgorithmDTO(GeneticAlgorithmBase, SolverDTO):
    selection: Union[TournamentSelectionDTO, NSGA2basedTournamentSelectionDTO]
    crossover: Union[OrderCrossoverDTO, PartiallyMappedCrossoverDTO, UniformOrderBasedCrossoverDTO, CycleCrossoverDTO, EdgeCrossoverDTO]
    mutation: Union[InversionMutationDTO, InsertMutationDTO, ScrambleMutationDTO, ShiftMutationDTO, SwapMutationDTO]
    survival: Union[TruncationSurvivalDTO, NSGA2basedSurvivalDTO]
