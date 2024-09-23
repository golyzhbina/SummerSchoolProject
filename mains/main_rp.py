import _cohpy
import numpy as np

from model.ModelCreator import ModelCreator
from parsing.DocParser import DocParser
from parsing.LasParser import LasParser
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.TracesReader import TracesReader
from region.RegionCreator import RegionCreator
from time_calculation.EikonalSolver import EikonalSolver
from time_calculation.TravelTimeCalculator_cohsum import TravelTimeCalculator

from processing_cube.start_processing import start
from time import time

receivers_coords = ReceiverCoordsHandler.read_coords("/home/golub/SummerSchoolProject/data/coords.xlsx")

traces = TracesReader.read_traces("/home/golub/SummerSchoolProject/data/00000215_276_22_14.18.0.sgy")
depths_las, speeds_las = LasParser.get_depths_and_speeds("/home/golub/SummerSchoolProject/data/306Merged_Set.las")
depths_vel, speeds_vel = DocParser.get_depths_and_speeds("/home/golub/SummerSchoolProject/data/vel.docx")
depths = np.hstack([depths_vel[0:65], depths_las])
speeds = np.hstack([speeds_vel[0:65], speeds_las])

step_on_net = 10
region = RegionCreator.create_region(9658000, 5857000, 9658500, 5857500, step_on_net)

#region = RegionCreator.create_region(0, 0, 0, 0, step_on_net)
#region.list_of_source = np.array([(9658360, 5857280)])

step_model = 10
model = ModelCreator.create_model(depths, speeds, receivers_coords, region, step_model)

depth = -1245
source = (int(round((depth - model.max_depth) / model.step, 0)), 0)
eikonal_solve = EikonalSolver.solve(model, source)

receivers_coords_on_net = ReceiverCoordsHandler.get_coords_on_net(receivers_coords, region.list_of_source, region.step)
travel_time = TravelTimeCalculator.get_times_for_all_source(eikonal_solve[-1] * 1000, receivers_coords_on_net)

tensor_matrix = np.array([1, 1, 1, 0, 0, 0])
region.list_of_source = np.hstack([region.list_of_source, np.array([[depth]] * region.list_of_source.shape[0])])
receivers_coords = np.hstack([receivers_coords, np.array([[0]] * receivers_coords.shape[0])])

result = _cohpy.PyEmissionTomography_dd().compute_emission_tomography_with_tensor_moment(traces.traces, 
											travel_time, 
											receivers_coords, 
											region.list_of_source, 
											tensor_matrix, 
											1, 
											need_divide_by_distance=True,
											)
#result = _cohpy.PyEmissionTomography_dd().compute_emission_tomography_without_tensor_moments(traces.traces, travel_time, 1)

result = result.reshape((region.amount_x, region.amount_y, -1))
#result = result.reshape((1, 1, -1))
print(result.shape)
start(result, result.shape)