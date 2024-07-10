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
