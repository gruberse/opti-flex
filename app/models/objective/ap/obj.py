import json
from typing import List, Any

import numpy as np
import requests

from app.models.fitness.obj import Fitness
from .base import AssignmentObjectiveBase
from ..obj import Objective


class AssignmentObjective(AssignmentObjectiveBase, Objective):
    transposed: bool = False
    matrix: Any = None

    def _get_fitness(self, encoding: List[int]):
        fitness = 0

        for i in range(len(encoding)):
            if encoding[i] > -1:
                fitness += self.matrix[i][encoding[i]]

        return Fitness(objective_id=self.objective_id, actual_fitness=fitness)


    def init_evaluation_setup(self) -> None:
        if self.matrix.shape[1] > self.matrix.shape[0]:
            self.matrix = self.matrix.T
            self.transposed = True

        if self.privacy_engine:
            try:
                decoder = json.JSONDecoder()

                # If the privacy engine is used for an imbalanced problem, a dummy column is added to the matrix
                # This column is later used to indicate no assignment
                if self.matrix.shape[0] != self.matrix.shape[1]:
                    dummy_column = np.zeros((self.matrix.shape[0], 1), dtype=np.float64)
                    self.matrix = np.column_stack((self.matrix, dummy_column))

                # Encode the weights and initialize a secret-shared session
                request_encode = requests.put(f'{self.encoding_url}', json=self.matrix.tolist())

                if request_encode.status_code == 200:
                    encoded_weights = decoder.decode(request_encode.content.decode())
                    _ = requests.put(f'{self.privacy_engine}/sessionSecret', json={'mapping': {}, 'weights': encoded_weights})
                else:
                    raise RuntimeError(f'Encoder is not available and objective {self.objective_id} cannot be initialized')

            except ConnectionError as e:
                raise RuntimeError(f'Encoder is not available and objective {self.objective_id} cannot be initialized')


def test():
    objective = AssignmentObjective(objective_id="test", matrix=np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    assert objective._get_fitness([0, 1, 2]).actual_fitness == 1 + 5 + 9
    assert objective._get_fitness([0, 2, 1]).actual_fitness == 1 + 8 + 6
    assert objective._get_fitness([1, 0, 2]).actual_fitness == 4 + 2 + 9
    assert objective._get_fitness([1, 2, 0]).actual_fitness == 4 + 8 + 3
    assert objective._get_fitness([2, 0, 1]).actual_fitness == 7 + 2 + 6
    assert objective._get_fitness([2, 1, 0]).actual_fitness == 7 + 5 + 3
