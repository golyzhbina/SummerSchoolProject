import numpy as np

from region.Region import Region
from time_calculation.TravelTimeCalcutator import TravelTimeCalculator
from cube.CoherenceCube import CoherenceCube
from model.Model import Model
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.Traces import Traces
# from geo import create_cube

class CoherenceCubeCreator:
    
    @staticmethod
    def create_cube(
                    region: Region,
                    traces: Traces,
                    travel_time,
                    time_interval: tuple,
                    dt,
                    depth) -> CoherenceCube:

        cube = create_cube(travel_time, traces.traces, time_interval[0], time_interval[1])
        return CoherenceCube(cube,
                             (region.start_x, region.start_y),
                             (region.amount_x, region.amount_y),
                             region.step,
                             time_interval,
                             dt,
                             depth)

    @staticmethod
    def get_times_for_all_source(time_travel: np.ndarray, receivers_coords_on_net: np.ndarray, start_time: int) -> np.ndarray:
        times_for_all_source = list()

        for i in range(len(receivers_coords_on_net)):
            times_for_source = list()
            receivers_coords_on_net[i] = sorted(receivers_coords_on_net[i], key=lambda x: x[1])
            for receiver in receivers_coords_on_net[i]:
                times_for_source.append(int(round(time_travel[receiver[0]], 0)) + start_time)

            times_for_all_source.append(np.array(times_for_source))

        return np.array(times_for_all_source)
