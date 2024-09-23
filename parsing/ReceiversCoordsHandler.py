import numpy as np
import pandas as pd

distance = lambda x1, y1, x2, y2: np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class ReceiverCoordsHandler:

    @staticmethod
    def read_coords(filename: str) -> np.ndarray:

        f = open(filename, "r")
        data = f.readline()
        coords = []
        while data != "":
            data = data.split()
            coords.append(np.array([float(data[0]), float(data[1])]))
            data = f.readline()
        
        return np.array(coords)

    @staticmethod
    def __get_coords_as_indexes(coords: np.ndarray, source: tuple, step: int) -> np.ndarray:
        indexes = [(int(distance(coords[i][0], coords[i][1], source[0], source[1]) / step), i) for i in range(coords.shape[0])]
        return np.array(indexes)

    @staticmethod
    def get_coords_on_net(coords: np.ndarray, source_coords: np.ndarray, step: int) -> np.ndarray:
        coords_on_net = list()
        for source in source_coords:
            coords_on_net.append(ReceiverCoordsHandler.__get_coords_as_indexes(coords, source, step))

        return np.array(coords_on_net)

