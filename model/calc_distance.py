import numpy as np


def calc_distance(source: tuple, receivers: np.array) -> np.ndarray:
    return np.array(
        [np.sqrt((source[0] - coords[0]) ** 2 + (source[1] - coords[1]) ** 2) for coords in receivers]
    )