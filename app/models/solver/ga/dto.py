from typing import Union

from app.models.solver.dto import SolverDTO
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.pmx.dto import PartiallyMatchedCrossoverDTO
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.fitness_evaluation.combined.dto import CombinedEvaluationDTO
from app.models.solver.ga.fitness_evaluation.elitists.dto import ElitistsEvaluationDTO
from app.models.solver.ga.fitness_evaluation.offspring.dto import OffspringEvaluationDTO
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.dto import NSGA2BasedTournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.survivor_selection.elitists.dto import ElitistsSelectionDTO
from app.models.solver.ga.survivor_selection.elitists_nsga2.dto import NSGA2BasedElitistsSelectionDTO


class GeneticAlgorithmDTO(GeneticAlgorithmBase, SolverDTO):
    parent_selection: Union[TournamentSelectionDTO, NSGA2BasedTournamentSelectionDTO]
    crossover: Union[OrderCrossoverDTO, PartiallyMatchedCrossoverDTO, UniformOrderBasedCrossoverDTO, CycleCrossoverDTO]
    mutation: Union[InversionMutationDTO, InsertMutationDTO, ScrambleMutationDTO, ShiftMutationDTO, SwapMutationDTO]
    fitness_evaluation: Union[OffspringEvaluationDTO, ElitistsEvaluationDTO, CombinedEvaluationDTO]
    survivor_selection: Union[ElitistsSelectionDTO, NSGA2BasedElitistsSelectionDTO]
