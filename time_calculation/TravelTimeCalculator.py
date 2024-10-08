from model.Model import Model
import numpy as np
from math import sqrt

class TravelTimeCalculator:

    @staticmethod
    def get_times_as_inds_with_vel_model(time_travel: np.ndarray, receivers_coords_on_net: np.ndarray) -> np.ndarray:
        times_for_all_source = list()

        for i in range(len(receivers_coords_on_net)):
            times_for_source = list()
            receivers_coords_on_net[i] = sorted(receivers_coords_on_net[i], key=lambda x: x[1])
            for receiver in receivers_coords_on_net[i]:
                times_for_source.append(time_travel[receiver[0]])
            local_min = min(times_for_source)
            times_for_source = [int(n - local_min) for n in times_for_source]
            times_for_all_source.append(np.array(times_for_source))

        return np.array(times_for_all_source)
    
    @staticmethod
    def get_times_with_vel_model(time_travel: np.ndarray, receivers_coords_on_net: np.ndarray) -> np.ndarray:
        times_for_all_source = list()

        for i in range(len(receivers_coords_on_net)):
            times_for_source = list()
            receivers_coords_on_net[i] = sorted(receivers_coords_on_net[i], key=lambda x: x[1])
            for receiver in receivers_coords_on_net[i]:
                times_for_source.append(time_travel[receiver[0]])

            times_for_all_source.append(np.array(times_for_source))

        return np.array(times_for_all_source)

    @staticmethod
    def get_times_with_const_vel(receiver_coords: np.ndarray, source_coords: np.ndarray, vel: float) -> np.ndarray:

        timess = []
        distance = lambda x1, x2, y1, y2: sqrt((x1 - x2) **2 + (y1 - y2) **2)
        for i in range(source_coords.shape[0]):
            times = []
            for j in range(receiver_coords.shape[0]):
                times.append(distance(source_coords[i][0], receiver_coords[j][0], source_coords[i][1], receiver_coords[j][1]) / vel)
            timess.append(np.array(times) * 1000)
        return np.array(timess)
