import numpy as np

from Region import Region
from TravelTimeCalcutator import TravelTimeCalculator
from cube.CoherenceCube import CoherenceCube
from model.Model import Model
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.Traces import Traces


class CubeCoherenceCreator:
    def create_cube(self,
                    region: Region,
                    traces: Traces,
                    model: Model,
                    receivers_coords: np.ndarray,
                    time_interval,
                    dt = 1) -> CoherenceCube:

        len_of_interval = time_interval[1] - time_interval[0]
        max_depth = model.field.shape[0]
        max_distance = model.field.shape[1]
        cube = np.zeros((max_depth, max_distance, len_of_interval))

        tt_calculator = TravelTimeCalculator()
        handler = ReceiverCoordsHandler()
        receivers_coords_on_net = handler.get_coords_as_indexes(receivers_coords,
                                                                region.start_x,
                                                                region.start_y,
                                                                model.step)
        for depth in range(max_depth):
            time_travel = tt_calculator.calc_travel_time(model, (depth, 0))[-1]
            for distance in range(max_distance):
                receivers_coords_on_net_shifted = handler.shift_indexes(max_distance, receivers_coords_on_net, distance)
                t0 = time_interval[0]
                for k in range(len_of_interval):
                    integral = 0
                    for receiver in receivers_coords_on_net_shifted:
                        t = time_travel[receiver[0]] + t0
                        index_in_trace = int(round(t / traces.sample_interval, 0))
                        integral += traces.traces[receiver[1]][index_in_trace]

                    cube[depth][distance][k] = integral
                    t0 += dt

                print(f"calc for {depth}/{max_depth}, {distance}/{max_distance}")
        return CoherenceCube(cube, region, time_interval, dt)