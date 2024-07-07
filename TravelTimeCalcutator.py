from model.Model import Model
import numpy as np
import eikonalfm


class TravelTimeCalculator:
    def calc_travel_time(self, model: Model, source: tuple) -> np.ndarray:
        times = eikonalfm.factored_fast_marching(model.field, source, (model.step, model.step), 2)
        distance = eikonalfm.distance(times.shape,  x_s=source, dx=(model.step, model.step), indexing="ij")
        return times * distance
