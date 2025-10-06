from typing import Union

from app.models.solver.dto import SolverDTO
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.pmx.dto import PartiallyMatchedCrossoverDTO
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.parent_selection.nsga2.dto import NSGA2ParentSelectionDTO
from app.models.solver.ga.parent_selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.survivor_selection.offspring.dto import OffspringSelectionDTO
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2SurvivorSelectionDTO


class GeneticAlgorithmDTO(GeneticAlgorithmBase, SolverDTO):
    parent_selection: Union[TournamentSelectionDTO, NSGA2ParentSelectionDTO]
    crossover: Union[OrderCrossoverDTO, PartiallyMatchedCrossoverDTO, UniformOrderBasedCrossoverDTO, CycleCrossoverDTO]
    mutation: Union[InversionMutationDTO, InsertMutationDTO, ScrambleMutationDTO, ShiftMutationDTO, SwapMutationDTO]
    survivor_selection: Union[OffspringSelectionDTO, NSGA2SurvivorSelectionDTO]
