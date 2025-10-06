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
from app.models.solver.ga.fitness_evaluation.obj import FitnessEvaluation
from app.models.solver.ga.mutation.obj import Mutation
from app.models.solver.ga.parent_selection.obj import ParentSelection
from app.models.solver.ga.survivor_selection.obj import SurvivorSelection
from app.models.solver.obj import Solver


class GeneticAlgorithm(GeneticAlgorithmBase, Solver):
    parent_selection: ParentSelection
    crossover: Crossover
    mutation: Mutation
    fitness_evaluation: FitnessEvaluation
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
        population = Population(population_id=0, start_time=datetime.now())

        candidates = []
        for _ in range(self.population_size):
            candidates.append(Individual(encoding=random.sample(gene_space, problem_size)))

        # calculate the fitness of the initial population
        candidates = self.fitness_evaluation.evaluate_individuals(problem, [], candidates)

        # survivor selection
        survivors = self.survivor_selection.select_survivors(self.population_size, candidates)

        population.individuals = survivors
        population.end_time = datetime.now()
        populations.append(population)

        population_queue.put(population.population_id)

        # main loop
        for population_id in range(1, self.generations + 1):
            # initialize the next generation
            population = Population(population_id=population_id, start_time=datetime.now())

            # select the parents
            selected_parents = self.parent_selection.select_parents(survivors)

            # apply crossover
            offspring = self.crossover.crossover_parents(selected_parents)

            # apply mutation
            offspring = self.mutation.mutate_offspring(offspring)

            # calculate the fitness of the generational
            # offspring = problem.evaluate_individuals(offspring)
            evaluated_individuals = self.fitness_evaluation.evaluate_individuals(problem, populations[-1].individuals, offspring)

            # survivor selection
            survivors = self.survivor_selection.select_survivors(self.population_size, evaluated_individuals)

            population.individuals = survivors
            population.end_time = datetime.now()

            populations.append(population)
            population_queue.put(population.population_id)

        # stop the population process
        population_queue.put(None)
