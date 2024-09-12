import _cohpy
import numpy as np

from model.ModelCreator import ModelCreator
from parsing.DocParser import DocParser
from parsing.LasParser import LasParser
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.TracesReader import TracesReader
from region.RegionCreator import RegionCreator
from time_calculation.EikonalSolver import EikonalSolver
from time_calculation.TravelTimeCalcutator import TravelTimeCalculator

from processing_cube.start_processing import start
from time import time

step_on_net = 1
region = RegionCreator.create_region(-75, -75, 75, 75, step_on_net)

receivers_coords = ReceiverCoordsHandler.read_from_txt("/home/golub/SummerSchoolProject/data/coord.txt")
receivers_coords_on_net = ReceiverCoordsHandler.get_coords_on_net(receivers_coords, region.list_of_source, region.step)

travel_time = TravelTimeCalculator.get_times_for_all_source_new(receivers_coords, region.list_of_source)


traces = TracesReader.read_traces("/home/golub/SummerSchoolProject/data/8723_z_filtered.sgy")
print(max(np.max(time) for time in travel_time))

result = _cohpy.PyEmissionTomography_dd().compute_emission_tomography_without_tensor_moments(traces.traces, travel_time, 1)
#result = _cohpy.PyEmissionTomography_dd().compute_emission_tomography_without_tensor_moments(traces.traces, travel_time, 1)

result = result.reshape((region.amount_x, region.amount_y, -1))
#result = result.reshape((1, 1, -1))
print(result.shape)
start(result, result.shape)