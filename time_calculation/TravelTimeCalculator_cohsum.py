from model.Model import Model
import numpy as np
import eikonalfm


class TravelTimeCalculator:

    @staticmethod
    def get_times_for_all_source(time_travel: np.ndarray, receivers_coords_on_net: np.ndarray) -> np.ndarray:
        times_for_all_source = list()

        for i in range(len(receivers_coords_on_net)):
            times_for_source = list()
            receivers_coords_on_net[i] = sorted(receivers_coords_on_net[i], key=lambda x: x[1])
            for receiver in receivers_coords_on_net[i]:
                times_for_source.append(time_travel[receiver[0]])

            times_for_all_source.append(np.array(times_for_source))

        return np.array(times_for_all_source)