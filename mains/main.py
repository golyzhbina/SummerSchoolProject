import numpy as np

from cube.CoherenceCubeCreator import CoherenceCubeCreator
from model.ModelCreator import ModelCreator
from parsing.DocParser import DocParser
from parsing.LasParser import LasParser
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from traces.TracesReader import TracesReader
from region.RegionCreator import RegionCreator
from time_calculation.EikonalSolver import EikonalSolver
from SummerSchoolProject.time_calculation.TravelTimeCalculator import TravelTimeCalculator


step_on_net = 10
region = RegionCreator.create_region(9658000, 5857000, 9658500, 5857500, step_on_net)

receivers_coords = ReceiverCoordsHandler.read_coords("start_data\\coords.xlsx")
receivers_coords_on_net = ReceiverCoordsHandler.get_coords_on_net(receivers_coords, region.list_of_source, region.step)

traces = TracesReader.read_traces("C:\\Users\\golub\\test2\\pythonProject1\\start_data\\00000215_276_22_14.18.0.sgy")
depths_las, speeds_las = LasParser.get_depths_and_speeds("..\\start_data\\306Merged_Set.las")
depths_vel, speeds_vel = DocParser.get_depths_and_speeds("start_data\\vel.docx")
depths = np.hstack([depths_vel[0:65], depths_las])
speeds = np.hstack([speeds_vel[0:65], speeds_las])

step_model = 10
model = ModelCreator.create_model(depths, speeds, receivers_coords, region, step_model)


interval = (14300, 14400)
depth = -1245
source = (int(round((depth - model.max_depth) / model.step, 0)), 0)

eikonal_solve = EikonalSolver.solve(model, source)
travel_time = TravelTimeCalculator.get_times_for_all_source(eikonal_solve[-1] * 1000, receivers_coords_on_net, interval[0])
cube = CoherenceCubeCreator.create_cube(region, traces, travel_time, interval, traces.sample_interval, depth)
