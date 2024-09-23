from CoherentSummationModule import CoherentSummation as Cohsum
import numpy as np

from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.TracesReader import TracesReader
from region.RegionCreator import RegionCreator
from SummerSchoolProject.time_calculation.TravelTimeCalculator import TravelTimeCalculator
from cumsun.CumSumCalculator import CumSumCalculator
from processing_cube.start_processing import start

step_on_net = 1
region = RegionCreator.create_region(0, 0, 150, 150, step_on_net)

receivers_coords = ReceiverCoordsHandler.read_coords("/home/golub/SummerSchoolProject/data/coords/coord_2.txt")
travel_time = TravelTimeCalculator.get_times_with_const_vel(receivers_coords, region.list_of_source, 300)
traces = TracesReader.read_traces("/home/golub/SummerSchoolProject/data/sgy/8730_z_filtered.sgy")


result = Cohsum().compute_emission_tomography_without_tensor_moments(traces.traces, travel_time, 1)
result = CumSumCalculator.get_cumsum(result, 100)

result = result.reshape((region.amount_x, region.amount_y, -1))
print(result.shape)
start(result)