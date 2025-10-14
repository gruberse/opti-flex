import multiprocessing
import random
from datetime import datetime
from typing import List, Optional

import numpy as np

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.re_evaluation.obj import ReEvaluation
from app.models.solver.ga.environmental_selection.obj import EnvironmentalSelection
from app.models.solver.obj import Solver


class GeneticAlgorithm(GeneticAlgorithmBase, Solver):
    parent_selection: ParentSelection
    crossover: Crossover
    mutation: Mutation
    re_evaluation: ReEvaluation
    environmental_selection: EnvironmentalSelection


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

        # environmental selection
        selected_individuals = self.environmental_selection.select_individuals(
            individuals=candidates,
            n_individuals=self.population_size
        )

        initial_population.individuals = selected_individuals
        initial_population.end_time = datetime.now()
        populations.append(initial_population)

        population_queue.put(initial_population.population_id)

        # main loop
        for population_id in range(1, self.n_generations + 1):
            # initialize the next generation
            current_population = Population(population_id=population_id, start_time=datetime.now())

            # select the parents
            selected_parents = self.parent_selection.select_individuals(
                individuals=selected_individuals,
                n_parents=self.n_parents
            )

            # apply crossover
            offspring = self.crossover.crossover_parents(
                parents=selected_parents,
                n_offspring=self.re_evaluation.get_remaining_population_size(
                    population_size=self.population_size
                )
            )

            # apply mutation
            mutated_offspring = self.mutation.mutate_offspring(offspring=offspring)

            # select individuals for evaluation
            evaluation_individuals = self.re_evaluation.select_evaluation_individuals(
                parents=populations[-1].individuals,
                offspring=mutated_offspring,
                survival_selection=self.environmental_selection
            )

            # evaluate fitness
            evaluated_individuals = problem.evaluate_individuals(individuals=evaluation_individuals)

            # environmental selection
            selected_individuals = self.environmental_selection.select_individuals(
                individuals=evaluated_individuals,
                n_individuals=self.population_size
            )

            current_population.individuals = selected_individuals
            current_population.end_time = datetime.now()

            populations.append(current_population)
            population_queue.put(current_population.population_id)

        # stop the population process
        population_queue.put(None)
