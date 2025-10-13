import multiprocessing
import random
from datetime import datetime
from typing import List, Any

import numpy as np

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.re_evaluation.obj import ReEvaluation
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection
from app.models.solver.obj import Solver


class GeneticAlgorithm(GeneticAlgorithmBase, Solver):
    parent_selection: ParentSelection
    crossover: Crossover
    mutation: Mutation
    re_evaluation: ReEvaluation
    survivor_selection: SurvivorSelection


    def solve(self, problem: Problem, population_queue: multiprocessing.Queue, populations: List) -> None:
        # retrieve the gene and problem space from the problem
        gene_space = problem.get_gene_space()
        problem_size = problem.get_problem_size()

        # set the random seed
        if self.random_seed is not None:
            random.seed(self.random_seed)
            np.random.seed(self.random_seed)

        # create the initial population
        initial_population = Population(population_id=0, start_time=datetime.now())

        candidates = []
        for _ in range(self.population_size):
            candidates.append(Individual(encoding=random.sample(gene_space, problem_size)))

        # calculate the fitness of the initial population
        candidates = problem.evaluate_individuals(candidates)

        # survivor parent_selection
        survivors = self.survivor_selection.select_individuals(candidates, self.population_size)

        initial_population.individuals = survivors
        initial_population.end_time = datetime.now()
        populations.append(initial_population)

        population_queue.put(initial_population.population_id)

        # main loop
        for population_id in range(1, self.n_generations + 1):
            # initialize the next generation
            current_population = Population(population_id=population_id, start_time=datetime.now())

            # select the parents
            selected_parents = self.parent_selection.select_individuals(survivors, self.n_parents)

            # apply crossover
            offspring = self.crossover.crossover_parents(
                selected_parents,
                self.re_evaluation.get_remaining_population_size(self.population_size)
            )

            # apply mutation
            mutated_offspring = self.mutation.mutate_offspring(offspring)

            # select individuals for evaluation
            evaluation_individuals = self.re_evaluation.get_evaluation_individuals(
                populations[-1].individuals,
                mutated_offspring,
                self.survivor_selection
            )

            # evaluate fitness
            evaluated_individuals = problem.evaluate_individuals(evaluation_individuals)

            # survivor parent_selection
            survivors = self.survivor_selection.select_individuals(evaluated_individuals, self.population_size)

            current_population.individuals = survivors
            current_population.end_time = datetime.now()

            populations.append(current_population)
            population_queue.put(current_population.population_id)

        # stop the population process
        population_queue.put(None)
