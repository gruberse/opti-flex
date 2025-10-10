from typing import Union

from app.models.solver.dto import SolverDTO
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.cx.dto import CycleCrossoverDTO
from app.models.solver.ga.crossover.erx.dto import EdgeRecombinationCrossoverDTO
from app.models.solver.ga.crossover.ox.dto import OrderCrossoverDTO
from app.models.solver.ga.crossover.pmx.dto import PartiallyMatchedCrossoverDTO
from app.models.solver.ga.crossover.uox.dto import UniformOrderBasedCrossoverDTO
from app.models.solver.ga.mutation.insert.dto import InsertMutationDTO
from app.models.solver.ga.mutation.inversion.dto import InversionMutationDTO
from app.models.solver.ga.mutation.scramble.dto import ScrambleMutationDTO
from app.models.solver.ga.mutation.shift.dto import ShiftMutationDTO
from app.models.solver.ga.mutation.swap.dto import SwapMutationDTO
from app.models.solver.ga.parent_selection.tournament.dto import TournamentSelectionDTO
from app.models.solver.ga.parent_selection.tournament_nsga2.dto import NSGA2basedTournamentSelectionDTO
from app.models.solver.ga.re_evaluation.elitists.dto import ElitistsReEvaluationDTO
from app.models.solver.ga.re_evaluation.population.dto import PopulationReEvaluationDTO
from app.models.solver.ga.survivor_selection.nsga2.dto import NSGA2basedSurvivalSelectionDTO
from app.models.solver.ga.survivor_selection.truncation.dto import TruncationSelectionDTO


class GeneticAlgorithmDTO(GeneticAlgorithmBase, SolverDTO):
    parent_selection: Union[TournamentSelectionDTO, NSGA2basedTournamentSelectionDTO]
    crossover: Union[OrderCrossoverDTO, PartiallyMatchedCrossoverDTO, UniformOrderBasedCrossoverDTO, CycleCrossoverDTO, EdgeRecombinationCrossoverDTO]
    mutation: Union[InversionMutationDTO, InsertMutationDTO, ScrambleMutationDTO, ShiftMutationDTO, SwapMutationDTO]
    re_evaluation: Union[PopulationReEvaluationDTO, ElitistsReEvaluationDTO]
    survivor_selection: Union[TruncationSelectionDTO, NSGA2basedSurvivalSelectionDTO]
