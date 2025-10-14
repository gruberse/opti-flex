import multiprocessing
import random
from datetime import datetime
from typing import List

import numpy as np

from app.models.individual.obj import Individual
from app.models.population.obj import Population
from app.models.problem.obj import Problem
from app.models.solver.ga.base import GeneticAlgorithmBase
from app.models.solver.ga.crossover.obj import Crossover
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.selection.obj import Selection
from app.models.solver.ga.survival.obj import Survival
from app.models.solver.obj import Solver


class GeneticAlgorithm(GeneticAlgorithmBase, Solver):
    selection: Selection
    crossover: Crossover
    mutation: Mutation
    survival: Survival


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

        # create random individuals
        candidates = []
        for _ in range(self.population_size):
            candidates.append(Individual(encoding=random.sample(gene_space, problem_size)))

        # calculate the fitness of the initial population
        candidates = problem.evaluate_individuals(candidates)

        # environmental selection
        survivors = self.survival.select_individuals(
            individuals=candidates,
            n_individuals=self.population_size
        )

        initial_population.individuals = survivors
        initial_population.end_time = datetime.now()
        populations.append(initial_population)

        population_queue.put(initial_population.population_id)

        # set the remaining population size depending on the number of elitists
        remaining_population_size = self.population_size - self.n_elitists

        # main loop
        for population_id in range(1, self.n_generations + 1):
            # initialize the next generation
            current_population = Population(population_id=population_id, start_time=datetime.now())

            # select the parents
            selected_parents = self.selection.select_individuals(
                individuals=populations[-1].individuals,
                n_individuals=remaining_population_size + 1,
                # add 1 to address odd population sizes due to e.g. elitism
            )

            # apply crossover
            offspring = self.crossover.crossover_parents(
                parents=selected_parents,
                n_offspring=remaining_population_size,
            )

            # apply mutation
            mutated_offspring = self.mutation.mutate_offspring(offspring=offspring)

            # select individuals for evaluation
            evaluation_individuals = []
            evaluation_individuals.extend(mutated_offspring)

            #   add elitist individuals from the previous population
            if self.n_elitists > 0:
                evaluation_individuals.extend(
                    self.survival.select_individuals(
                        individuals=populations[-1].individuals,
                        n_individuals=self.n_elitists)
                )

            #   add the previous population for re-evaluation
            if self.re_evaluate_previous_population:
                evaluation_individuals.extend(populations[-1].individuals)

            # evaluate fitness
            evaluated_individuals = problem.evaluate_individuals(individuals=evaluation_individuals)

            # environmental selection
            survivors = self.survival.select_individuals(
                individuals=evaluated_individuals,
                n_individuals=self.population_size
            )

            current_population.individuals = survivors
            current_population.end_time = datetime.now()

            populations.append(current_population)
            population_queue.put(current_population.population_id)

        # stop the population process
        population_queue.put(None)
