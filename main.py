from cube.CoherenceCubeCreator import CoherenceCubeCreator
from model.ModelCreator import ModelCreator
from parsing.DocParser import DocParser
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from parsing.LasParser import LasParser
from traces.TracesReader import TracesReader
from region.RegionCreator import RegionCreator

step = 10
region = RegionCreator.create_region(9658000, 5857000, 9658500, 5857500, 10)
receivers_coords = ReceiverCoordsHandler.read_coords("start_data\\coords.xlsx")
traces = TracesReader.read_traces("C:\\Users\\golub\\test2\\pythonProject1\\start_data\\00000215_276_22_14.18.0.sgy")

depths, speeds = LasParser.get_depths_and_speeds("start_data\\306Merged_Set.las")
depthsv, speedsv = DocParser.get_depths_and_speeds("start_data\\vel.docx")
depths = depthsv[0:65] + depths
speeds = speedsv[0:65] + speeds
model = ModelCreator.create_model(depths, speeds, receivers_coords, region, step)

interval = (14300, 14400)
depth = -1245
cube = CoherenceCubeCreator.create_cube(region, traces, model, depth, receivers_coords, interval, traces.sample_interval)


file = open(f"got_data/{depth}_t34.txt",  "w")
file.write(f"{region.amount_y} {region.amount_x} {interval[0]} {interval[1]}\n")

for i in range(region.amount_y * region.amount_x):
        print(*cube.cube[i], sep=' ', end="\n", file=file)
file.close()
