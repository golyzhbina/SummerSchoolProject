import numpy as np

from region.Region import Region
from TravelTimeCalcutator import TravelTimeCalculator
from cube.CoherenceCube import CoherenceCube
from model.Model import Model
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.Traces import Traces
from geo import create_cube

class CoherenceCubeCreator:
    
    @staticmethod
    def create_cube(
                    region: Region,
                    traces: Traces,
                    model: Model,
                    depth: float,
                    receivers_coords: np.ndarray,
                    time_interval: tuple,
                    dt) -> CoherenceCube:

        len_of_interval = time_interval[1] - time_interval[0]
        handler = ReceiverCoordsHandler()

        abs_depth = int(round((depth - model.max_depth) / model.step, 0))
        tt_calculator = TravelTimeCalculator()
        time_travel = tt_calculator.calc_travel_time(model, (abs_depth, 0))[-1] * 1000   # in milliseconds
        receivers_coords_on_net = handler.get_coords_on_net(receivers_coords, region.list_of_source, model.step)
        times_for_all_source = CoherenceCubeCreator.get_times_for_all_source(time_travel, receivers_coords_on_net, time_interval[0])
        cube = create_cube(times_for_all_source, traces.traces, time_interval[0], time_interval[1])
        return CoherenceCube(cube, region, time_interval, dt, depth)

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
