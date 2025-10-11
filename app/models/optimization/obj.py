import multiprocessing
import uuid
from datetime import datetime
from typing import Any, List


from app.config import config
from app.models.enums.config import ApplicationMode
from .base import OptimizationBase
from .custom_process.process import Process
from ..enums.status import Status
from ..problem.obj import Problem
from ..solver.obj import Solver
from ..statistics.obj import Statistics


class Optimization(OptimizationBase):
    def __init__(self, /, **data):
        super().__init__(**data)

        application_mode = config.get("application", "mode")
        if application_mode == ApplicationMode.OPS.value:
            self.optimization_id = uuid.uuid4()
        elif application_mode == ApplicationMode.DEV.value:
            self.optimization_id = uuid.UUID('00000000-0000-0000-0000-000000000001')
        else:
            raise RuntimeError('invalid configuration for application mode')

        self.status = Status.CREATED

        self.manager = multiprocessing.Manager()

        self.population_queue = multiprocessing.Queue()

        self.statistics = Statistics(self.manager)

    problem: Problem
    solver: Solver
    statistics: Statistics = None

    manager: Any = None

    optimization_process: Any = None
    population_process: Any = None

    population_queue: Any = None

    def _shutdown_processes(self):
        if self.optimization_process:
            self.optimization_process.kill()
            self.optimization_process.join()

            self.population_queue.put(None)
            self.population_process.join()

    @staticmethod
    def _process_population(population_queue: multiprocessing.Queue, populations: List, time_optimization_stopped: multiprocessing.Value) -> None:
        i = population_queue.get(block=True)
        while i is not None:
            population = populations[i]

            population.non_dominated_individuals[:] = population.get_non_dominated_individuals()

            populations[i] = population

            i = population_queue.get(block=True)

        time_optimization_stopped.value = datetime.now().timestamp()


    def run(self, async_run: bool) -> bool:
        self.statistics.time_optimization_started.value = datetime.now().timestamp()
        try:
            self.optimization_process = Process(target=self.solver.solve,
                                                args=(self.problem,
                                                      self.population_queue,
                                                      self.statistics.populations),
                                                daemon=True)
            self.optimization_process.start()

            self.population_process = Process(target=self._process_population,
                                              args=(self.population_queue,
                                                    self.statistics.populations,
                                                    self.statistics.time_optimization_stopped),
                                              daemon=True)

            self.population_process.start()

            self.status = Status.RUNNING

            if not async_run:
                self.optimization_process.join()
                self.population_process.join()

            return True

        except Exception as e:
            self.status = Status.FAILED
            self._shutdown_processes()

            return False

    def abort(self) -> bool:
        if (self.optimization_process is None) or (not self.optimization_process.is_alive()):
            return False

        self._shutdown_processes()
        self.update()
        self.status = Status.ABORTED
        return True

    def update(self) -> None:
        # in the case of exception, do not provide a result
        if self.optimization_process and self.optimization_process.exception:
            self.status = Status.FAILED
            self._shutdown_processes()

        # check if update has already been called
        if self.status != Status.RUNNING:
            return

        # take the latest processed population
        if self.statistics.populations:
            for population in reversed(list(self.statistics.populations)):
                if population.non_dominated_individuals:
                    self.problem.update_result(population.non_dominated_individuals)
                    break

        # optimization finished
        if not self.optimization_process.is_alive() and not self.population_process.is_alive():
            self.status = Status.FINISHED
