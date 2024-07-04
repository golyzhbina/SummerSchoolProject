import numpy as np
import pandas as pd
from math import floor


class ReceiverCoordsHandler:

    def read_coords(self, filename: str) -> np.ndarray:
        file = pd.read_excel(filename, skiprows=1, index_col=[0, 1])
        return np.hsplit(file.values, 2)[0]

    def get_coords_as_indexes(self, coords: np.ndarray,  step: int) -> np.ndarray:
        new_centre_x = min(coords, key=lambda arr: arr[0])[0]
        new_centre_y = min(coords, key=lambda arr: arr[1])[1]
        centred_coords = [(pair - [new_centre_x, new_centre_y]) / step for pair in coords]
        centred_coords = np.array([np.array([int(centred_coords[i][0]), int(centred_coords[i][1]), i], dtype=int) for i in range(len(centred_coords))])
        return centred_coords