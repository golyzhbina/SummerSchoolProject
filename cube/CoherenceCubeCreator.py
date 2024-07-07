import numpy as np

from Region import Region
from TravelTimeCalcutator import TravelTimeCalculator
from cube.CoherenceCube import CoherenceCube
from model.Model import Model
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.Traces import Traces


class CoherenceCubeCreator:
    def create_cube(self,
                    region: Region,
                    traces: Traces,
                    model: Model,
                    depth,
                    receivers_coords: np.ndarray,
                    time_interval,
                    dt = 1) -> CoherenceCube:

        len_of_interval = time_interval[1] - time_interval[0]
        cube = np.zeros((region.amount_y * region.amount_x, len_of_interval))
        handler = ReceiverCoordsHandler()

        abs_depth = int(round((depth + model.max_depth) / model.step, 0))
        tt_calculator = TravelTimeCalculator()
        time_travel = tt_calculator.calc_travel_time(model, (abs_depth, 0))[-1]

        for i in range(len(region.list_op_points)):
            receivers_coords_on_net = handler.get_coords_as_indexes(receivers_coords, region.list_op_points[i], model.step)
            for receiver in receivers_coords_on_net:
                index_in_trace = int(round(time_travel[receiver[0]], 0)) + time_interval[0]
                for k in range(len_of_interval):
                    cube[i][k] += traces.traces[receiver[1]][index_in_trace]
                    index_in_trace += 1

            print(f"{i}/{len(region.list_op_points)}")
        return CoherenceCube(cube, region, time_interval, dt, depth)