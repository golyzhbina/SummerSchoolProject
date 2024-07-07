import numpy as np
import pandas as pd

distance = lambda x1, y1, x2, y2: np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class ReceiverCoordsHandler:

    def read_coords(self, filename: str) -> np.ndarray:
        file = pd.read_excel(filename, skiprows=1, index_col=[0, 1])
        return np.hsplit(file.values, 2)[0]

    def get_coords_as_indexes(self, coords: np.ndarray, source: tuple, step: int) -> list:
        indexes = [(int(distance(coords[i][0], coords[i][1], source[0], source[1]) / step), i) for i in range(coords.shape[0])]
        return indexes

    def shift_indexes(self, weigh: int,  indexes: list, shift: int) -> list:
        new_weigh = weigh - shift
        new_indexes = indexes.copy()

        for i in range(len(indexes)):
            if indexes[i][0] >= new_weigh:
                new_indexes.remove(indexes[i])
            elif indexes[i][0] <= shift:
                new_indexes.append(indexes[i])

        return new_indexes
