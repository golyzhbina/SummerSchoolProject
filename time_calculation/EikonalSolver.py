from model.Model import Model
import numpy as np
import eikonalfm


class EikonalSolver:

    @staticmethod
    def solve(model: Model, source: tuple) -> np.ndarray:
        times = eikonalfm.factored_fast_marching(model.field, source, (model.step, model.step), 2)
        distance = eikonalfm.distance(times.shape,  x_s=source, dx=(model.step, model.step), indexing="ij")
        return times * distance
