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

        # create the initial population
        population = Population(population_id=0, start_time=datetime.now())

        candidates = []
        for _ in range(self.population_size):
            candidates.append(Individual(encoding=random.sample(gene_space, problem_size)))

        # calculate the fitness of the initial population
        candidates = problem.evaluate_individuals(candidates)

        # survivor selection
        survivors = self.survivor_selection.select_survivors(candidates, self.population_size)

        population.individuals = survivors
        population.end_time = datetime.now()
        populations.append(population)

        population_queue.put(population.population_id)

        # main loop
        for population_id in range(1, self.generations + 1):
            # initialize the next generation
            population = Population(population_id=population_id, start_time=datetime.now())

            # select the parents
            selected_parents = self.parent_selection.select_parents(survivors, self.population_size)

            # apply crossover
            offspring = self.crossover.crossover_parents(selected_parents)

            # apply mutation
            offspring = self.mutation.mutate_offspring(offspring)

            # calculate the fitness of individuals
            # this mechanism allows to use elitism despite obfuscation
            # the estimated fitness depends on the composition of the population
            # re-evaluation of the parent population allows for a better comparison with the offspring

            # default = generational replacement
            evaluation_individuals = offspring

            # plus selection
            if self.re_evaluate == 'parents':
                evaluation_individuals = evaluation_individuals + populations[-1].individuals
            # elitist injection
            elif self.re_evaluate == 'elitists':
                # retrieve non dominated individuals (elitists) of the parent population
                non_dominated_individuals = populations[-1].non_dominated_individuals if populations[
                    -1].non_dominated_individuals else populations[-1].get_non_dominated_individuals()
                # randomly replace offspring individuals with the elitists of the parent population
                indices = sorted(random.sample(range(len(offspring) + 1), len(non_dominated_individuals)))
                for i, idx in enumerate(indices):
                    evaluation_individuals[idx] = non_dominated_individuals[i]

            evaluated_individuals = problem.evaluate_individuals(evaluation_individuals)

            # survivor selection
            survivors = self.survivor_selection.select_survivors(evaluated_individuals, self.population_size)

            population.individuals = survivors
            population.end_time = datetime.now()

            populations.append(population)
            population_queue.put(population.population_id)

        # stop the population process
        population_queue.put(None)
