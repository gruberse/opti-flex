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
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection
from app.models.solver.obj import Solver


class GeneticAlgorithm(GeneticAlgorithmBase, Solver):
    parent_selection: ParentSelection
    crossover: Crossover
    mutation: Mutation
    survivor_selection: SurvivorSelection

    def solve(self, problem: Problem, population_queue: multiprocessing.Queue, populations: List) -> None:
        # retrieve the gene and problem space from the problem
        gene_space = problem.get_gene_space()
        problem_size = problem.get_problem_size()

        # set the random seed
        if self.random_seed is not None:
            random.seed(self.random_seed)
            np.random.seed(self.random_seed)

        # set the generation counter
        current_generation = 0

        # create the initial population
        population = Population(population_id=current_generation, start_time=datetime.now())

        candidates = []
        for _ in range(self.population_size):
            candidates.append(Individual(encoding=random.sample(gene_space, problem_size)))

        # calculate the fitness of the initial population
        candidates = problem.evaluate_individuals(candidates)

        # survivor selection
        survivors = self.survivor_selection.select_survivors([], candidates)

        population.individuals = survivors
        population.end_time = datetime.now()
        populations.append(population)

        population_queue.put(population.population_id)

        # main loop
        while current_generation < self.generations:
            # increase the generation counter
            current_generation += 1

            # initialize the next generation
            population = Population(population_id=current_generation, start_time=datetime.now())

            # select the parents
            parents = self.parent_selection.select_parents(survivors)

            # apply crossover
            offspring = self.crossover.crossover_parents(parents)

            # apply mutation
            offspring = self.mutation.mutate_offspring(offspring)

            # calculate the fitness of the offspring
            offspring = problem.evaluate_individuals(offspring)

            # survivor selection
            survivors = self.survivor_selection.select_survivors(parents, offspring)

            population.individuals = survivors
            population.end_time = datetime.now()

            populations.append(population)
            population_queue.put(population.population_id)

        # stop the population process
        population_queue.put(None)
