import numpy as np

from cube.CoherenceCubeCreator import CoherenceCubeCreator
from model.ModelCreator import ModelCreator
from parsing.ReceiversCoordsHandler import ReceiverCoordsHandler
from TravelTimeCalcutator import TravelTimeCalculator
from traces.TracesReader import TracesReader
from Region import create_region

step = 10
region = create_region(9658000, 5857000, 9658500, 5857500, 10)
handler = ReceiverCoordsHandler()
receivers_coords = handler.read_coords("C:\\Users\\golub\\test2\\pythonProject1\\coords.xlsx")
traces = TracesReader().read_traces("C:\\Users\\golub\\Downloads\\Telegram Desktop\\00000215_276_22_14.18.0.sgy")
model = ModelCreator().create_model("/start_data/vel.docx",
                                    receivers_coords,
                                    region,
                                    step)

interval = (14400, 14500)
depth = -1245
cube = CoherenceCubeCreator().create_cube(region, traces, model, depth, receivers_coords, interval, traces.sample_interval)
file = open(f"{depth}_1.3.txt",  "w")
file.write(f"{region.amount_y} {region.amount_x} {interval[0]} {interval[1]}\n")

for i in range(region.amount_y * region.amount_x):
        print(*cube.cube[i], sep=' ', end="\n", file=file)
file.close()
